#!/usr/bin/python

def selection_sort_asc(arr):
    for i in range(0, len(arr)):
        min = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                index = j
        arr[index] = arr[i]
        arr[i] = min
    return arr

if __name__ == "__main__":
    arr = [3,7,4,5,2,1,2]
    arr = selection_sort_asc(arr)
    print arr
