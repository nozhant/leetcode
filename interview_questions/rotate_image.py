"""Rotate Image: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/770/
"""

class Solution:

    def rotate_image_inplace(self, matrix):
        """Time complexity: O(n2) Space complexity: O(1)"""

        n = len(matrix)
        # Transpose the Matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

    def rotate_image(self, matrix):
        """Time complexity: O(n2) Space complexity: O(n2)"""

        reverse_matrix = matrix[::-1]
        rotated_list = []
        for row in zip(*reverse_matrix):

            rotated_list.append(list(row))

        return rotated_list

    def rotate_image_optimized(self, matrix):
        """Time complexity: O(n²) Space complexity: O(n²) (same but in one line)"""

        return [list(row) for row in zip(*matrix[::-1])]


# Example usage:
# print(Solution().rotate_image_inplace([[1,2,3],[4,5,6],[7,8,9]]))

