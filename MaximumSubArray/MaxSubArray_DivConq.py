def max_cross(arr, low, mid, high):
    left_sum = None
    left_i = mid - 1
    i = mid - 1
    sum = 0
    while i >= 0:
        sum += arr[i]
        if (not left_sum) or (sum > left_sum):
            left_sum = sum
            left_i = i
        i -= 1

    right_sum = None
    right_j = mid
    j = mid
    sum = 0
    while j < high:
        sum += arr[j]
        if (not right_sum) or (sum > right_sum):
            right_sum = sum
            right_j = j
        j += 1
    return (left_i, right_j, left_sum + right_sum)

def max_sub(arr, low, high):
    if high - low <= 1:
        return (low, low, arr[low])
    mid = (low + high) // 2
    low_i, low_j, low_sum = max_sub(arr, low, mid)
    high_i, high_j, high_sum = max_sub(arr, mid, high)
    cross_i, cross_j, cross_sum = max_cross(arr, low, mid, high)
    if low_sum > high_sum and low_sum > cross_sum:
        return (low_i, low_j, low_sum)
    if high_sum > low_sum and high_sum > cross_sum:
        return (high_i, high_j, high_sum)
    return (cross_i, cross_j, cross_sum)



def max_subarray(arr):
    if not arr:
        return (None, None, None)
    return max_sub(arr, 0, len(arr))


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    i, j, s = max_subarray(arr)
    print("max sum {}, from {} to {}".format(s, i, j))

    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    i, j, s = max_subarray(arr)
    print("max sum {}, from {} to {}".format(s, i, j))

    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
    i, j, s = max_subarray(arr)
    print("max sum {}, from {} to {}".format(s, i, j))

    arr = [] 
    i, j, s = max_subarray(arr)
    print("max sum {}, from {} to {}".format(s, i, j))

    arr = [5] 
    i, j, s = max_subarray(arr)
    print("max sum {}, from {} to {}".format(s, i, j))

    arr = [1, -5] 
    i, j, s = max_subarray(arr)
    print("max sum {}, from {} to {}".format(s, i, j))
