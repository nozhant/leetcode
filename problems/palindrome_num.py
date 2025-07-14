"""Palindrome Number: Given an integer x, return true if x is a palindrome, and false otherwise.

link: https://leetcode.com/problems/palindrome-number/description/
"""


class Solution:

    def is_palindrome(self, x: int) -> bool:
        """Time complexity: O(n) Space complexity: O(n)"""

        string_num = str(x)
        return string_num == string_num[::-1]

# Example usage:
# print(Solution().is_palindrome(-121))