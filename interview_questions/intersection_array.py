"""Intersection of Two Arrays II: Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/
"""


from collections import Counter


class Solution:

    def intersect(self, nums1, nums2):
        """Time complexity: O(n) Space complexity: O(n)"""

        count1 = Counter(nums1)
        count2 = Counter(nums2)

        result = []
        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))

        return result

# Example Usage:
# print(Solution().intersect([4,9,5], [9,4,9,8,4]))



