def linear_search(arr, target):
    for num in range(len(arr)):
        if arr[num] == target:
            return num
    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

        else:
            return mid
    return -1  # not found
