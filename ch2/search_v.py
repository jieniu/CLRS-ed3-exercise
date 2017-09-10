#!/usr/bin/python

# exercise 2.1-3
# if v exist in arr, return i; otherwise return nil
# 循环不变式描述：
# 1. 在循环之前，从数组的第一个元素开始考察
# 2. 在下一次循环之前，对元素和v进行比较，如果相同会返回当前的下标，否则下标+1，考察下一个元素
# 3.  # 在循环结束时，如果没有找到v，则是遍历了数组的所有元素的，此时返回None, 另一种情况下是找到了v，则返回下标
def search_v(arr, v):
    for i in range(0, len(arr)):
        if arr[i] == v:
            return i
    return None

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,8,7]
    print search_v(arr, 7)
    print search_v(arr, 17)

