import numpy as NUM

def bubbleSort(x):
    length = len(x)
    if length <= 1:
        return x

    for i in range(length):
        for j in range(i + 1, length):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x

def selectionSort(x):
    length = len(x)
    if length <= 1:
        return x

    for i in range(length):
        minimum = NUM.min(x[i:])
        if x[i] > minimum:
            j = NUM.where(x == minimum)[0][-1]
            x[i], x[j] = x[j], x[i]
    return x

def mergeSort(x):
    from heapq import merge
    length = len(x)
    if length <= 1:
        return x

    middle = length //2
    left = x[0:middle]
    right = x[middle:]

    left = mergeSort(left)
    right = mergeSort(right)

    return list(merge(left, right))

def quickSort(x):
    length = len(x)
    if length <= 1:
        return x

    pivot = x[0]
    less = quickSort([i for i in x[1:] if i < pivot])
    more = quickSort([i for i in x[1:] if i >= pivot])
    return less + [pivot] + more

def bucketSort(x):
    length = len(x)
    if length <= 1:
        return x

    count = NUM.zeros(length)
    for i in x:
        count[i] += 1
    x = []
    for n, amount in enumerate(count):
        x.extend([n] * amount)
    return x


if __name__ == '__main__':
    x = NUM.random.randint(0, 100, 100)
    print (x)
