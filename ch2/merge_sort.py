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
    while i < len(left):
        if j >= len(right):
            break
        if left[i] < right[j]:
            arr[i+j] = left[i]
            i += 1
        else:
            arr[i+j] = right[j]
            j += 1

    if i == len(left):
        arr[i+j:] = right[j:]
    else:
        arr[i+j:] = left[i:]


if __name__ == "__main__":
    a = [0,0,1,2,2,3,1,4,5,7,8,9,99,100,101]
    merge(a, 0, 6, 15)
    print a
