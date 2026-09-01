from typing import List

class Solution:
    def merge_sorted_arrays(
        self, arr_1: List[int], m: int, arr_2: List[int], n: int
    ) -> None:
        # Iterate from the end
        index1      = m - 1  
        index2      = n - 1
        index_write = m + n - 1     # Write in values

        while index1 >= 0 and index2 >= 0:
            if arr_1[index1] > arr_2[index2]:
                arr_1[index_write] = arr_1[index1]
                index1 -= 1
            else:
                arr_1[index_write] = arr_2[index2]
                index2 -= 1
            # Both cases, once something is written, write moves back
            index_write -= 1

        # Case of leftover elements in arr_2
        while index2 >= 0:
            arr_1[index_write] = arr_2[index2]  # Array is sorted already so just write in, moving back
            index2 -= 1
            index_write -= 1

        # note that if arr1 has leftovers when p2 < 0,
        # elements already in place since array is sorted

        