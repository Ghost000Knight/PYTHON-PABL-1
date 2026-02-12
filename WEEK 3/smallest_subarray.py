class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        
        start = 0
        curr_sum = 0
        min_len = float('inf')
        
        for end in range(n):
            curr_sum += arr[end]
            
            # Shrink window while sum is greater than x
            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1
        
        # If no valid subarray found
        if min_len == float('inf'):
            return 0
        
        return min_len
