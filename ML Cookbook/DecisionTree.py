"""
:Author: james
:Date: 21/10/2019
:License: MIT

:name: DecisionTree.py

Basic implementation of a binary decision tree algorithm, with one
discriminant per node.
"""

import numpy as np
from sklearn import datasets


def proportion_k(ym):
    """
    Get the proportions of each class in the current set of values.

    :param ym: y values (class) of the data at a given node.
    :return:
    """
    counts = list(np.unique(ym, return_counts=True))
    counts[1] = counts[1]/(ym.shape[0])
    return counts


def gini(k_proportions):
    """
    Gini impurity function.

    :param k_proportions:
    :return:
    """
    return (k_proportions*(1-k_proportions)).sum()


def node_impurity(ym):
    """
    Calculate the impurity of data at a given node of the tree.

    :param ym:
    :return:
    """
    if ym.shape[0] == 0:
        return {"impurity": 0, "max_group": 0}
    k_prop = proportion_k(ym)
    return {"impurity": gini(k_prop[1]), "max_group": k_prop[0][np.argmax(k_prop[1])]}


def disc_val_impurity(yleft, yright):
    """
    Calculate the level of impurity left in the given data split.

    :param yleft:
    :param yright:
    :return:
    """
    nleft = yleft.shape[0]
    nright = yright.shape[0]
    ntot = nleft + nright
    left_imp = node_impurity(yleft)
    right_imp = node_impurity(yright)

    return {
        "impurity": ((nleft/ntot)*left_imp["impurity"])+((nright/ntot)*right_imp["impurity"]),
        "lmax_group": left_imp["max_group"],
        "rmax_group": right_imp["max_group"]
    }


def niave_min_impurity(xm, ym):
    minxs = xm.min(axis=0)
    maxxs = xm.max(axis=0)

    # discriminator with the smallest impurity.
    cur_min_disc = None

    for x_idx, (dmin, dmax) in enumerate(zip(minxs, maxxs)):
        disc_vals = np.linspace(dmin, dmax, 10)
        for disc_val in disc_vals:
            selection = xm[:, x_idx] < disc_val
            yleft = ym[selection]
            yright = ym[selection==False]
            imp = disc_val_impurity(yleft, yright)
            try:
                if cur_min_disc["impurity"] > imp["impurity"]:
                    imp["discriminator"] = x_idx
                    imp["val"] = disc_val
                    cur_min_disc = imp
            except TypeError:
                imp["discriminator"] = x_idx
                imp["val"] = disc_val
                cur_min_disc = imp

    return cur_min_disc


class BinaryTreeClassifier:

    def __init__(self, max_depth=4, min_data=5):
        tree = dict()
        self.depth = max_depth
        self.min_data = min_data

    def _node_mask(X, node):
        return X[:, node["discriminator"]] < node["val"]

    def _apply_disc(X, y, node):
        left_cond = BinaryTreeClassifier._node_mask(X, node)
        right_cond = left_cond == False
        left_X, left_y = X[left_cond], y[left_cond]
        right_X, right_y = X[right_cond], y[right_cond]

        return left_X, left_y, right_X, right_y

    def _tree_node(X, y, max_depth, min_data):
        node = niave_min_impurity(X, y)
        left_X, left_y, right_X, right_y = BinaryTreeClassifier._apply_disc(X, y, node)

        if max_depth > 0:
            if left_X.shape[0] >= min_data:
                node["left"] = BinaryTreeClassifier._tree_node(left_X, left_y, max_depth-1, min_data)
            if right_X.shape[0] >= min_data:
                node["right"] = BinaryTreeClassifier._tree_node(right_X, right_y, max_depth-1, min_data)

        return node

    def _run_tree(X, node):
        y = np.zeros(X.shape[0])
        left_cond = BinaryTreeClassifier._node_mask(X, node)
        right_cond = left_cond == False
        try:
            y[left_cond] = BinaryTreeClassifier._run_tree(X[left_cond], node["left"])
        except KeyError:
            y[left_cond] = node["lmax_group"]
        try:
            y[right_cond] = BinaryTreeClassifier._run_tree(X[right_cond], node["right"])
        except KeyError:
            y[right_cond] = node["rmax_group"]

        return y

    def _node_dict(node, idx=0):
        nodes = {}
        node_data = {"lmax_group": node["lmax_group"],
                     "rmax_group": node["rmax_group"],
                     "discriminator": node["discriminator"],
                     "val": node["val"]}
        nodes[idx] = node_data
        try:
            left_idx = 2 * idx + 1
            nodes.update(BinaryTreeClassifier._node_dict(node["left"], left_idx))
        except KeyError:
            pass

        try:
            right_idx = 2 * idx + 2
            nodes.update(BinaryTreeClassifier._node_dict(node["right"], right_idx))
        except KeyError:
            pass

        return nodes

    def build_tree(self, X, y):
        self.tree = BinaryTreeClassifier._tree_node(X, y, self.depth, self.min_data)

    def classify(self, X):
        return BinaryTreeClassifier._run_tree(X, self.tree)

    def tree_to_heap_array(self):
        tree_dict = BinaryTreeClassifier._node_dict(self.tree)
        return [tree_dict[key] for key in sorted(tree_dict.keys())]


def shuffle_split(x, y, frac=0.6):
    """
    Shuffle and split X and y data.

    :param x:
    :param y:
    :param frac:
    :return:
    """
    data_idx = np.arange(x.shape[0])
    sample1 = data_idx < (data_idx.max()*frac)
    np.random.shuffle(data_idx)
    np.random.shuffle(sample1)
    sample2 = sample1 == False
    x1, y1 = x[data_idx[sample1]], y[data_idx[sample1]]
    x2, y2 = x[data_idx[sample2]], y[data_idx[sample2]]
    return x1, y1, x2, y2


if __name__ == "__main__":
    np.random.seed(10)
    iris_data = datasets.load_iris()
    X = iris_data["data"]
    y = iris_data["target"]
    X_train, y_train, X_test, y_test = shuffle_split(X, y)
    classifier = BinaryTreeClassifier()
    classifier.build_tree(X_train, y_train)
    result = classifier.classify(X_test)
    print("accuracy:", (result == y_test).sum()/(result.shape[0]))
    tree_arr = classifier.tree_to_heap_array()
    pass
