""" K-th Smallest in Lexicographical Order: Given two integers n and k, return the kth lexicographically
smallest integer in the range [1, n].

link: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description
"""

class Solution:

    def find_kth_number(self, n, k) -> int:
        """Time complexity: O(log² n) Space complexity: O(1)"""

        def count_steps(prefix, n):
            steps = 0
            first, last = prefix, prefix
            while first <= n:
                steps += min(n + 1, last + 1) - first
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr

# Example Usage:

#print(Solution().find_kth_number(13, 2))
