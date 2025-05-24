"""
This module defines a Solution class with two methods to find the largest number
in a list that is less than or equal to a given target.
One method uses a linear scan (O(n)), and the other uses binary search (O(log n))
for sorted lists.
"""

class Solution:
    def find_max_linear(self, nums, target):
        """Time Complexity: O(n) Space Complexity: O(k), where k is the number of elements <= target
        """
        valid = [num for num in nums if num <= target]
        return max(valid) if valid else None

    def find_max_binary(self, nums, target):
        """(Assumes nums is sorted in ascending order) Time Complexity: O(log n) Space Complexity: O(1)"""
        import bisect
        idx = bisect.bisect_right(nums, target)
        return nums[idx - 1] if idx > 0 else None

# Example usage:
# nums = [1000, 1100, 1200, 1450, 1650]
# target = 1199
#
# sol = Solution()
# print("Linear version result:", sol.find_max_linear(nums, target))
# print("Binary search version result:", sol.find_max_binary(nums, target))