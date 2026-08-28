
from typing import List


class Solution:
    def column_major_traversal(
        self, matrix: List[List[int]]
    ) -> List[int]:

        # Handles empty matrix
        if not matrix or not matrix[0]:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        result: List[int] = []


        for col in range(cols):
            for row in range(rows):
                result.append(matrix[row][col])
        
        return result
