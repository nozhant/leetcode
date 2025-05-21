from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int):

        len_nums = len(nums)

        if len_nums < 2 or k <= 0:
            # No change if the list has fewer than 2 elements or if k is non-positive
            return

        k = k % len_nums  # To handle cases where k > len(nums)
        if k == 0:  # If k is exactly a multiple of the length, no change is needed
            return

        # if k > len_nums:
        #     nums[:] = nums[-len_nums:] + nums[:-len_nums]
        # else:
        nums[:] = nums[-k:] + nums[:-k]

        return nums

s = Solution()
print(s.rotate(nums=[1,2], k=3))



