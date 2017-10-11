#!/usr/bin/python

# arr = array
# p = head index
# q = middle index
# r = tail index
# the two sub array is sorted
def merge(arr, p, q, r):
    left = [x for x in arr[p:q]]
    right = [x for x in arr[q:r]]

    i = 0
    j = 0
    inversions = 0
    while i < len(left):
        if j >= len(right):
            break
        if left[i] <= right[j]:
            arr[p+i+j] = left[i]
            i += 1
        else:
            arr[p+i+j] = right[j]
            j += 1
            inversions += len(left) - i

    if i == len(left):
        arr[p+i+j:r] = right[j:len(right)]
    else:
        arr[p+i+j:r] = left[i:len(left)]

    return inversions


def merge_sort(arr, p, r):
    inversions = 0
    if p+1 >= r:
        return 0

    q = (p + r)/2
    inversions += merge_sort(arr, p, q)
    inversions += merge_sort(arr, q, r)
    inversions += merge(arr, p, q, r)
    return inversions


if __name__ == "__main__":
    a = [0,0,1,2,2,3,1,4,5,7,8,9,99,100,101]
    merge(a, 0, 6, len(a))
    print a

    a = [5,2,4,7,1,3,2,6]
    inv = merge_sort(a, 0, len(a))
    print a
    print inv

    a = [2,3,8,6,1]
    inv = merge_sort(a, 0, len(a))
    print a
    print inv

