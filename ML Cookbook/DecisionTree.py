"""
:Author: James Sherratt
:Date: 21/10/2019
:License: MIT

:name: DecisionTree.py

Basic implementation of a binary decision tree algorithm, with one
discriminant per node.

Useful links:
https://scikit-learn.org/stable/modules/tree.html
https://en.wikipedia.org/wiki/Decision_tree
"""

import numpy as np
from sklearn import datasets


def proportion_k(ym):
    """
    Get the proportions of each class in the current set of values.

    :param ym: y values (class) of the data at a given node.
    :return: list containing the classes and the fraction of those classes present.
    """
    counts = list(np.unique(ym, return_counts=True))
    counts[1] = counts[1]/(ym.shape[0])
    return counts


def gini(k_proportions):
    """
    Gini impurity function. This is used to determine the impurity of a given
    set of data, given the proportions of the classes in the dataset.

    This is equivalent to:
    H = ∑ pk(1-pk) for all k classes.

    k_proportions, in this case, is an array of pk's

    :param k_proportions: array containing proportions of different classes. Proportions sum to 1.
    :return: the impurity of the dataset.
    """
    return (k_proportions*(1-k_proportions)).sum()


def node_impurity(ym):
    """
    Calculate the impurity of data on one side of node after split.

    :param ym: Actual y data for the selected dataset.
    :return: dict containing the impurity value of the side and the most common class on that side.
    """
    if ym.shape[0] == 0:
        return {"impurity": 0, "max_class": 0}
    k_prop = proportion_k(ym)
    return {"impurity": gini(k_prop[1]), "max_class": k_prop[0][np.argmax(k_prop[1])]}


def disc_val_impurity(yleft, yright):
    """
    Calculate the level of impurity left in the given data after splitting. This returns
    a dict which contains:

    - The impurity of the data after being split.
    - The class of the largest proportion on the left and right side of the split.

    The aim is to find a split which minimises impurity.

    The impurity calculated is:
    G = (nleft/ntot)*Hleft + (nright/ntot)*Hright

    This gives the impurity of the split data.

    :param yleft: Real/ training y values for the data on the left.
    :param yright: Real/ training y values for the data on the right.
    :return: Dict containing the data impurity after split and the most common class on the left and right of the split.
    """
    nleft = yleft.shape[0]
    nright = yright.shape[0]
    ntot = nleft + nright
    left_imp = node_impurity(yleft)
    right_imp = node_impurity(yright)

    return {
        "impurity": ((nleft/ntot)*left_imp["impurity"])+((nright/ntot)*right_imp["impurity"]),
        "lmax_class": left_imp["max_class"],
        "rmax_class": right_imp["max_class"]
    }


def niave_min_impurity(xm, ym):
    """
    Find a discriminator which minimises the impurity of the data. The discriminator
    is used to split data at a node.

    This works by:
    1. Selecting a data column as a discriminator.
    2. Splitting the possible values of the discriminator into 1000 even spaced values
    (between the minimum and maximum value in the dataset).
    3. Selecting the discriminator column + value which minimises the impurity.

    :param xm: Data on the left.
    :param ym: Data on the right.
    :return: dict containing the current niave minimum impurity.
    """
    minxs = xm.min(axis=0)
    maxxs = xm.max(axis=0)

    # discriminator with the smallest impurity.
    cur_min_disc = None

    # Choose a column to discriminate by.
    for x_idx, (dmin, dmax) in enumerate(zip(minxs, maxxs)):
        # Create a set of possibly values to use as the discriminator for that column.
        disc_vals = np.linspace(dmin, dmax, 1000)
        for disc_val in disc_vals:
            selection = xm[:, x_idx] < disc_val
            yleft = ym[selection]
            yright = ym[selection==False]
            # Calculate impurity.
            imp = disc_val_impurity(yleft, yright)
            # Choose a column with the smallest impurity.
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
        """
        Initialise the binary decision tree classifier. This classifier works by:
        - Splitting the data into 2 sets at every node.
        - These 2 sets are then split into 2 more sets at their nodes etc. until they reach a leaf.
        - At the leaves, the data is classified into whatever class was "most common" in that leaf during training.

        :param max_depth: The maximum depth the binary tree classifier goes to.
        :param min_data: The minimum sample size of the training data before the tree stops splitting.
        """
        tree = dict()
        self.depth = max_depth
        self.min_data = min_data

    def _node_mask(X, node):
        """
        Get the discriminator mask for the node. This splits the data into left and right components.

        :param X: dataset input data.
        :param node: the current node of the tree, with its discriminator value.
        :return: truth array, which splits data left and right.
        """
        return X[:, node["discriminator"]] < node["val"]

    def _apply_disc(X, y, node):
        """
        Apply the discriminator to the data at a given node.

        :param X: dataset input.
        :param y: dataset (observed) output.
        :param node: The node to split data by.
        :return: The x and y data, split left and right.
        """
        left_cond = BinaryTreeClassifier._node_mask(X, node)
        right_cond = left_cond == False
        left_X, left_y = X[left_cond], y[left_cond]
        right_X, right_y = X[right_cond], y[right_cond]

        return left_X, left_y, right_X, right_y

    def _tree_node(X, y, max_depth, min_data):
        """
        Create a tree node. This also creates child nodes of this node recursively.

        :param X: input data for the dataset at a node.
        :param y: output (observed) data for the dataset at a node.
        :param max_depth: The maximum depth of the tree from this node.
        :param min_data: The minimum amount of data which can be discriminated.
        :return: The node + its children, as a dict.
        """
        # Get the new node, as a dict.
        node = niave_min_impurity(X, y)
        # Split the data using the discriminator.
        left_X, left_y, right_X, right_y = BinaryTreeClassifier._apply_disc(X, y, node)

        if max_depth > 1:
            if left_X.shape[0] >= min_data:
                # Create a new node on the left (recursively) if max depth
                # and min data have not been reached.
                node["left"] = BinaryTreeClassifier._tree_node(left_X, left_y, max_depth-1, min_data)
            if right_X.shape[0] >= min_data:
                # Create a new node on the right (recursively) if max depth
                # and min data have not been reached.
                node["right"] = BinaryTreeClassifier._tree_node(right_X, right_y, max_depth-1, min_data)

        return node

    def _run_tree(X, node):
        """
        Run a node of the classifier, recurisively.

        :param node: The node to run on the data.
        :return: The classified y (expected) data.
        """
        # Setup y array.
        y = np.zeros(X.shape[0])
        # Get the discriminator left conditional.
        left_cond = BinaryTreeClassifier._node_mask(X, node)
        # Right conditional
        right_cond = left_cond == False
        try:
            # Try to split the data further on the left side.
            y[left_cond] = BinaryTreeClassifier._run_tree(X[left_cond], node["left"])
        except KeyError:
            # If we cannot split any further, get the class of the data on the left (as this is a leaf).
            y[left_cond] = node["lmax_class"]
        try:
            # Try to split the data further on the right side.
            y[right_cond] = BinaryTreeClassifier._run_tree(X[right_cond], node["right"])
        except KeyError:
            # If we cannot split any further, get the class of the data on the right (as this is a leaf).
            y[right_cond] = node["rmax_class"]

        return y

    def _node_dict(node, idx=0):
        """
        Get a dict of all the nodes, recursively. The keys are the index of an array,
        as if the array is a heap.

        :param node: The current node to add to the dict and to get children of recursively.
        :param idx: current index (key) of the node.
        :return: dict containing all the nodes retrieved.
        """
        # Current nodes.
        nodes = {}
        node_data = {"lmax_class": node["lmax_class"],
                     "rmax_class": node["rmax_class"],
                     "discriminator": node["discriminator"],
                     "val": node["val"]}
        nodes[idx] = node_data

        # Try to get the left nodes.
        try:
            left_idx = 2 * idx + 1
            nodes.update(BinaryTreeClassifier._node_dict(node["left"], left_idx))
        except KeyError:
            pass

        # Try to get the right nodes.
        try:
            right_idx = 2 * idx + 2
            nodes.update(BinaryTreeClassifier._node_dict(node["right"], right_idx))
        except KeyError:
            pass

        # return the dict of nodes retrieved.
        return nodes

    def build_tree(self, X, y):
        """
        Build (train) the decision tree classifier.

        :param X: input training data.
        :param y: output training (observed) data.
        :return: None
        """
        self.tree = BinaryTreeClassifier._tree_node(X, y, self.depth, self.min_data)

    def classify(self, X):
        """
        Classify some data using the tree.

        :param X: Input data.
        :return: output (expected) classes of the data, or y values, for the given input.
        """
        return BinaryTreeClassifier._run_tree(X, self.tree)

    def tree_to_heap_array(self):
        """
        Convert the tree to a binary heap, stored in an array with standard indexing.
        i.e. a node at index i has children at 2i*1 and 2i+2 and a parent at (i-1)//2.

        :return: list containing the tree nodes.
        """
        tree_dict = BinaryTreeClassifier._node_dict(self.tree)
        return [tree_dict[key] for key in sorted(tree_dict.keys())]


def shuffle_split(x, y, frac=0.6):
    """
    Shuffle and split X and y data. "frac" is the ratio of the split.
    e.g. 0.6 means 60% of the data goes into the left fraction, 40% into the right.
    Note X and y are shuffled the same, so row i in X data is still matched with row i in y after shuffle.

    :param x: X values of the data (predictor).
    :param y: y values of the data (observation).
    :param frac: fraction to split data by.
    :return: x1, y1, x2, y2 data where x1, y1 is the left fraction and x2, y2 is the right.
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
    # Set the seed for expected test results.
    np.random.seed(10)
    # Test decision tree with iris data.
    iris_data = datasets.load_iris()
    X = iris_data["data"]
    y = iris_data["target"]
    # Split iris data into test and train.
    X_train, y_train, X_test, y_test = shuffle_split(X, y)
    # create the decision tree classifier.
    classifier = BinaryTreeClassifier()
    # Train the classifier.
    classifier.build_tree(X_train, y_train)
    # Get the result when the classifier is applied to to the test data.
    result = classifier.classify(X_test)
    # Get the accuracy of the classifier.
    # accuracy = (number of correct results)/(total number of results)
    print("accuracy:", (result == y_test).sum()/(result.shape[0]))
    # convert the tree into a heap array.
    tree_arr = classifier.tree_to_heap_array()
    print("heap:")
    for i, node in enumerate(tree_arr):
        print(i, node)
