# Approach: Brute Force

def max_sum_subarray1(arr):
    n = len(arr)
    max_sum = arr[0]
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum = curr_sum + arr[j]
            max_sum = max(max_sum, curr_sum)
    
    return max_sum

# Approach: Kadane's Algorithm

def max_sum_subarray2(arr):
    n = len(arr)
    max_sum = arr[0]
    curr_sum = arr[0]
    
    for i in range(1, n):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum
