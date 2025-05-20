"""Two Sum: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/
"""

class Solution:

    def hash_table(self, nums, target):
        """Time complexity: O(n) Space complexity: O(n)"""

        num_indices = {}
        for index, num in enumerate(nums):

            diff = target - num
            print(diff)
            if diff in nums:
                return [num_indices[diff], index]

            num_indices[num] = index

        return []

    def bruteforce(self, nums, target):
        """Time complexity: O(n2) Space complexity: O(1)"""

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


print(Solution().hash_table([7,1, 6, 2, 4, 3], 5))