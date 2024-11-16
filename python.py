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
    max_sum = 0
    curr_sum = 0
    
    for i in range(n):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sum_subarray2(arr)) # 6