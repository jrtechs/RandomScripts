def radix_sort(lista):
    max_len = max([len(numero) for numero in lista])
    padded = list([str(num).rjust(max_len, "0") for num in lista])

    for pos in reversed(range(max_len)):
        buckets = [list() for x in range(0, 10)]
        for num in padded:
            bucket = int(num[pos])
            buckets[bucket] += [num]
        padded = sum(buckets, [])
    return padded

if __name__ == "__main__":
    print(radix_sort(["13", "105", "10", "150"]))
