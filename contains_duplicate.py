"""Contains Duplicate: Given an integer array nums, return true if any value appears at least twice in the array, and return false if
every element is distinct.

link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
"""

from typing import List


class Solution:

    def has_duplicate(self, nums: List[int]) -> bool:
        """Time complexity: O(n) Space complexity: O(n)"""

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Example usage:
# s = Solution()
# print(s.has_duplicate(nums=[0,4,5,0,3,6]))
