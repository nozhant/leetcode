class Solution:
    @staticmethod
    def find_target(nums, target):

        num_indices = {}
        for index, num in enumerate(nums):

            diff = target - num
            if diff in num_indices:
                return [num_indices[diff], index]

            num_indices[num] = index

        return []

print(Solution.find_target([7,1, 6, 2, 4, 3], 5))