
from typing import List


class Solution:
    def reverse(self, arr: List[int], left: int, right: int) -> None:
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def k_rotations(self, arr: List[int], k: int) -> None:
        length = len(arr)

        # Keeps k within range of the length - avoids indexing issues
        k %= length

        ## Note: Rotating right means reverse-whole-than-parts
        # Reverse whole
        self.reverse(arr, 0, length - 1)

        # Reverse first k elements
        self.reverse(arr, 0, k - 1)

        # Reverse last elements
        self.reverse(arr, k, length - 1)
        
