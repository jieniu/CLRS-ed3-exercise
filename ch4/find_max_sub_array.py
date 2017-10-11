#!/usr/bin/python

# CLRS page 71
def findMaximumSubArray(arr, start, end):
    if start == end - 1:
        return (start, end, arr[start])

    mid = (start + end) / 2
    (left_begin, left_end, left_sum) = findMaximumSubArray(arr, start, mid)
    (right_begin, right_end, right_sum) = findMaximumSubArray(arr, mid, end)
    (cross_left, cross_right, cross_sum) = findMaxCrossingSubarray(arr[start:end], mid - start)

    if left_sum > right_sum and left_sum > cross_sum:
        return (left_begin, left_end, left_sum)
    elif right_sum > left_sum and right_sum > cross_sum:
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
        if left_sum > left_max:
            left_max = left_sum
            begin = offset

    offset = mid
    end = offset
    right_max = array[offset]
    right_sum = right_max
    while offset < len(array) - 1:
        offset += 1
        right_sum += array[offset]
        if right_sum > right_max:
            right_max = right_sum
            end = offset

    return (begin, end, left_max + right_max)


if __name__ == "__main__":
    arr = [1,2,3,4,-7,6]
    print findMaxCrossingSubarray(arr, 3)

    # example in page 70
    arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    print findMaxSubArray(arr, 0, len(arr))
