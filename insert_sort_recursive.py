#!/usr/bin/python

def insert_sort_recursive(arr, length):
    if length > 2:
        insert_sort_recursive(arr, length - 1)

    value = arr[length - 1]
    j = length - 1
    for i in range(length - 2, -1, -1):
        if value >= arr[i]:
            break
        else:
            arr[i + 1] = arr[i]
            j = i
    arr[j] = value


if __name__ == "__main__":
    arr = [10,9,11,8,7,6,23]
    insert_sort_recursive(arr, len(arr))
    print arr



