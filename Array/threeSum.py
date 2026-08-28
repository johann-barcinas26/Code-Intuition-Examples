from typing import List

class Solution:
    def handle_dupe_left(self, arr: List[int], left: int, right: int) -> int:
        while left < right and arr[left] == arr[left + 1]:
            left += 1
        return left

    def handle_dupe_right(self, arr: List[int], left: int, right: int) -> int:
        while left < right and arr[right] == arr[right - 1]:
            right -= 1
        return right

    def two_sum(self, arr: List[int], index: int, result: List[List[int]]) -> None:
        left = index + 1       # Want subarray right of index
        right = len(arr) - 1

        while (left < right):
            current_sum = arr[index] + arr[left] + arr[right]
            # Match found
            if current_sum == 0:
                result.append([arr[index], arr[left], arr[right]])
                left = self.handle_dupe_left(arr, left, right)
                right = self.handle_dupe_right(arr, left, right)

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1



    def three_sum(self, arr: List[int]) -> List[List[int]]:
        result = []

        # Array empty
        if not arr:
            return []

        # Sort the array
        arr.sort()

        # Iterate through array looking for sums
        for i in range(len(arr) - 2):           # Leaves enough space for three operands
            if i > 0 and arr[i] == arr[i - 1]:  # Skips dupes after matches within an index
                continue            
            
            self.two_sum(arr, i, result)        
        
        return result

