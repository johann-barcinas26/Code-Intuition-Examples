from typing import List

class Solution:
    def two_sum(self, arr: List[int], target: int) -> List[int]:
        # List empty
        if not arr:
            return []

        # Sorts array from least to greatest
        arr.sort()

        # Use two pointers to determine target sum
        left = 0
        right = len(arr) - 1

        # arr[i] + arr[j] = target
        # 
        # Increasing left if sum < target
        # Increasing right if sum > target
        while (left < right):
            # If the target sum is found
            if (arr[left] + arr[right] == target):
                return [arr[left],arr[right]]

            # Cases of 
            if (arr[left] + arr[right] < target):
                left += 1
            elif (arr[left] + arr[right] > target):
                right -= 1
        
        return []