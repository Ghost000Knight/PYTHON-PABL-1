class Solution:
    def minSwap(self, arr, k):
        
        n = len(arr)
        
        # Step 1: Count elements <= k
        count = 0
        for i in range(n):
            if arr[i] <= k:
                count += 1
        
        if count == 0:
            return 0
        
        # Step 2: Count bad elements in first window
        bad = 0
        for i in range(count):
            if arr[i] > k:
                bad += 1
        
        ans = bad
        
        # Step 3: Slide window
        i = 0
        j = count
        
        while j < n:
            
            if arr[i] > k:
                bad -= 1
            
            if arr[j] > k:
                bad += 1
            
            ans = min(ans, bad)
            
            i += 1
            j += 1
        
        return ans
