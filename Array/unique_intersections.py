
from typing import List


class Solution:
    def unique_intersections(
        self, arr_1: List[int], arr_2: List[int]
    ) -> List[int]:

        # Using sets as there is no duplicates and is a O(1) way of searching
        result = set()
        seen = set(arr_1)

        for value in arr_2:
            if value in seen:
                result.add(value)
        
        return list(result)