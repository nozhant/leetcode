from typing import List


class Solution:
    def has_duplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        nums.sort()
        print(nums)
        for i in range(len(nums)):

            if nums[i] == nums[i-1]:
                return True
        return False


s = Solution()

print(s.has_duplicate(nums=[0,4,5,0,3,6]))
