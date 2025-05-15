from collections import Counter


class Solution:
    @staticmethod
    def intersect(nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        result = []
        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))

        return result


print(Solution().intersect([4,9,5], [9,4,9,8,4]))



