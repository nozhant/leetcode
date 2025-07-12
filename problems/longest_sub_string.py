"""Longest Substring Without Repeating Characters: Given a string s, find the length of the longest substring without duplicate characters.

link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:

    def length_of_longest_substring(self, s: str) -> int:
        """Time complexity: O(n) Space complexity: O(n)"""

        char_index = {}
        max_len = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = end
            max_len = max(max_len, end - start + 1)

        return max_len

# Example usage:
# print(Solution().length_of_longest_substring("abcabcbb"))



