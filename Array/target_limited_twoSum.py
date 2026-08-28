from typing import List

class Solution:
    def target_limited_two_sum(self, arr: List[int], target: int) -> int:
        # Sort array 
        arr.sort()

        # Two pointers to determine sums
        left = 0
        right = len(arr) - 1
        best = -1   # Value to check the best sum under target so far
        
        # Find the maximum sum thats less than the target (if existing)
        # Couldn't we find the max, and then move right pointer to decrease?
        while (left < right):
            # If target hit, reduce the sum
            if (arr[left] + arr[right] == target):
                right -= 1

            # Compare current best to new sum
            if (arr[left] + arr[right] < target):
                best = max(best, arr[left] + arr[right])
                left += 1
            elif (arr[left] + arr[right] > target):
                right -= 1

        return best