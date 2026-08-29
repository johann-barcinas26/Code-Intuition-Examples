from typing import List

class Solution:
    def two_sum(self, arr: List[int], index: int, target: int, result: int) -> int:
        left  = index + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[index] + arr[left] + arr[right]
            if abs(current_sum - target) < abs(result - target):
                result = current_sum
        
            if current_sum < target:
                left += 1
            else:
                right -= 1

        return result

    def approximate_three_sum(self, arr: List[int], target: int) -> int:
        best_sum: int = 0

        # Array empty
        if not arr:
            return 0

        # Loop through index - for each i perform a two_sum
        arr.sort()
        best_sum = arr[0] + arr[1] + arr[2]     # Initialize so real sums are compared

        for i in range(len(arr) - 2):
            best_sum = self.two_sum(arr, i, target, best_sum)
        
        return best_sum

