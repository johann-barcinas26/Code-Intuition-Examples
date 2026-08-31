from typing import List

class Solution:
    def skip_left_dupes(self, arr: List[int], left: int, right: int) -> int:
        while left < right and arr[left] == arr[left + 1]:
            left += 1

        return left
        
    def skip_right_dupes(self, arr: List[int], left: int, right: int) -> int:
        while left < right and arr[right] == arr[right - 1]:
            right -= 1

        return right
    
    def target_two_sum(self, arr: List[int], a: int, b: int, target: int, result: List[List[int]]) -> List[List[int]]:
        left  = b + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[a] + arr[b] + arr[left] + arr[right]

            if current_sum == target:
                result.append([arr[a], arr[b], arr[left], arr[right]])
                left  = self.skip_left_dupes(arr, left, right)
                right = self.skip_right_dupes(arr, left, right)

                left += 1
                right -= 1
            
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return result
            

    def four_sum(self, arr: List[int], target: int) -> List[List[int]]:
        result = []
        arr.sort()

        # Iterate through two outer loops before getting to a two sum
        for a in range(len(arr) - 3):
            if a > 0 and arr[a] == arr[a - 1]: 
                continue
            
            # Three-sum
            for b in range(a + 1, len(arr) - 2):
                if b > a + 1 and arr[b] == arr[b - 1]:
                    continue
                
                ### two sum logic
                result = self.target_two_sum(arr, a, b, target, result)
        
        return result

                