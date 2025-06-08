"""Lexicographical Numbers: Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.

link: https://leetcode.com/problems/lexicographical-numbers/description/
"""

class Solution:

    def lexical_order(self, n: int):
        """Time complexity: O(n) Space complexity: O(1)"""

        result = []
        curr = 1
        for _ in range(n):
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10
            elif curr % 10 != 9 and curr + 1 <= n:
                curr += 1
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return result

# Example Usage:
# print(Solution().lexical_order(13))
