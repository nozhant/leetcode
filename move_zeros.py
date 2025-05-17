class Solution:

    def move_zeroes(self, nums):
        insert_pos = 0  # Position to place the next non-zero

        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

        return nums


print(Solution().move_zeroes([0,1,0,3,12]))