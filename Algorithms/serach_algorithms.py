


def linear_search(arr,target):
    for key,value in enumerate(arr):
        if value == target:
            return key
    return -1

def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while(not left>right):
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1
    