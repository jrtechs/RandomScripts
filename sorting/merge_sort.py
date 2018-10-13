def merge_sort(a):
    if len(a) < 2:
        return a
    l = a[0:len(a)//2]
    r = a[len(a)//2:]
    return merge(merge_sort(l), merge_sort(r))


def merge(a, b):
    out = []
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if i >= len(a):
            out.append(b[j])
            j += 1
        elif j >= len(b):
            out.append(a[i])
            i += 1
        else:
            if a[i] <= b[j]:
                out.append(a[i])
                i += 1
            else:
                out.append(b[j])
                j += 1
    return out
