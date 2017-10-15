#!/usr/bin/python
#coding:utf-8

import random, datetime

# CLRS page 71
def findMaximumSubArray(arr, start, end):
    if start == end - 1:
        return (start, end, arr[start])

    mid = (start + end) / 2
    (left_begin, left_end, left_sum) = findMaximumSubArray(arr, start, mid)
    (right_begin, right_end, right_sum) = findMaximumSubArray(arr, mid, end)
    (cross_left, cross_right, cross_sum) = findMaxCrossingSubarray(arr[start:end], mid - start)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_begin, left_end, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_begin, right_end, right_sum)
    else:
        return (start+cross_left, start+cross_right, cross_sum)

def findMaxCrossingSubarray(array, mid):
    offset = mid - 1
    begin = offset
    left_max = array[offset]
    left_sum = left_max
    while offset > 0:
        offset -= 1
        left_sum += array[offset]
        if left_sum >= left_max:
            left_max = left_sum
            begin = offset

    offset = mid
    end = offset
    right_max = array[offset]
    right_sum = right_max
    while offset < len(array) - 1:
        offset += 1
        right_sum += array[offset]
        if right_sum >= right_max:
            right_max = right_sum
            end = offset

    return (begin, end, left_max + right_max)

# 求最大子数组的暴力版本
def findMaximumSubArrayBruteForceV(arr):
    max_sub = arr[0]
    begin = 0
    end = 0

    for i in range(0, len(arr)):
        sub_sum = 0
        for j in range(i, len(arr)):
            sub_sum += arr[j]
            if sub_sum >= max_sub:
                max_sub = sub_sum
                begin = i
                end = j
    return (begin, end, max_sub)

# 线性复杂度求最大子数组问题
def findMaximumSubArrayLinear(arr):
    left = 0
    right = 0
    temp_left = 0
    temp_sum = 0
    sum_max = arr[0]

    for i in range(0, len(arr)):
        if temp_sum + arr[i] <= arr[i]:
            temp_left = i
            temp_sum = arr[i]
        else:
            temp_sum += arr[i]

        if temp_sum > sum_max:
            sum_max = temp_sum
            right = i
            left = temp_left

    return (left, right, sum_max)

def computeCrossN():
    for i in range(2, 50):
        random.seed(i)
        arr = []
        for j in range(0, i):
            num = random.randint(-1000, 1000)
            arr.append(num)

        start = datetime.datetime.now()
        findMaximumSubArrayLinear(arr)
        end = datetime.datetime.now()
        delta3 = (end - start).microseconds * 1.0 / 1000

        start = datetime.datetime.now()
        findMaximumSubArray(arr, 0, len(arr))
        end = datetime.datetime.now()
        delta1 = (end - start).microseconds * 1.0 / 1000

        start = datetime.datetime.now()
        findMaximumSubArrayBruteForceV(arr)
        end = datetime.datetime.now()
        delta2 = (end - start).microseconds * 1.0 / 1000

        if delta1 < delta2:
            print "crossover n = %d" % i
            print "O(nlogN) %f, O(N^2) %f, O(N) %f" % (delta1, delta2, delta3)
            break
        else:
            print "O(nlogN) %f, O(N^2) %f, O(N) %f" % (delta1, delta2, delta3)


if __name__ == "__main__":

    computeCrossN()

    arr = [1,2,3,4,-7,6]
    print findMaxCrossingSubarray(arr, 3)
    print findMaximumSubArrayBruteForceV(arr)
    print findMaximumSubArrayLinear(arr)
    arr = [-1,-2,-3,-4,-7,-6]
    print findMaximumSubArrayLinear(arr)
    arr = [20,-3,-1,-7,11,1,-22]
    print findMaximumSubArrayLinear(arr)
    arr = [20,-3,-1,-7,11,1,-21, 1, 2,19]
    print findMaximumSubArrayLinear(arr)
    print findMaximumSubArray(arr, 0, len(arr))
    print findMaximumSubArrayBruteForceV(arr)

    # example in page 70
    arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    print findMaximumSubArray(arr, 0, len(arr))
    print findMaximumSubArrayBruteForceV(arr)
    print findMaximumSubArrayLinear(arr)

    arr = [-1,-2,-3,-4,-5]
    print findMaximumSubArrayBruteForceV(arr)

    arr = [-2,-3,-4,-5, -1]
    print findMaximumSubArrayBruteForceV(arr)
