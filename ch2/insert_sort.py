#!/usr/bin/python

def insertSortDesc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        key_index = i
        for j in range(i-1, -1, -1):
            if key <= arr[j]:
                break
            arr[j+1] = arr[j]
            key_index = j
        arr[key_index] = key
    return arr


if __name__ == "__main__":
    arr = [1,2,3,3,5,8,6]
    sortedArr = insertSortDesc(arr)
    print sortedArr
