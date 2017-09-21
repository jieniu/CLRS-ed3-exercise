#!/usr/bin/python

# return index if find but -1 if not
def binary_search(arr, p, q, value):

    index = (q + p) / 2
    if p > q or index >= len(arr):
        return -1

    if arr[index] == value:
        return index
    elif arr[index] < value:
        return binary_search(arr, index+1, q, value)
    else:
        return binary_search(arr, p, index-1, value)


if __name__ == "__main__":
    arr = [1]
    print binary_search(arr, 0, 0, 2)
    print binary_search(arr, 0, 0, 1)
    arr = [1,2,3,4,5,6,7,8,9,10,11]
    print binary_search(arr, 0, len(arr), 13)
    print binary_search(arr, 0, len(arr), 0)
    print binary_search(arr, 0, len(arr), 7)
