class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        # If students are more than packets
        if m > n:
            return -1
        
        # Sort the array
        arr.sort()
        
        # Initialize minimum difference
        min_diff = float('inf')
        
        # Slide window of size m
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff
