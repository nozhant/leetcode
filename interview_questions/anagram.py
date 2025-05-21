"""Typical anagram problem and easy solution (for kids!)"""

from collections import Counter


class Solution:

    def anagram_sorted(self, s, t):
        """Time complexity: O(n log n) Space complexity: O(n)"""

        return sorted(s) == sorted(t)

    def anagram_counter(self, s, t):
        """Time complexity: O(n) Space complexity: if the character set is fixed (e.g., lowercase English letters) O(1), O(n) but in the general case"""

        return Counter(s) == Counter(t)

# Example usage:
# print(anagram("rat", "car"))