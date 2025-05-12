from typing import List


class Solution:
    @staticmethod
    def longest_common_prefix(strs):
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]
        print("1", strs[0])

        # Iterate over the remaining strings
        for s in strs[1:]:
            # Reduce the prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                print(prefix)
                if not prefix:
                    return ""

        return prefix


print(Solution.longest_common_prefix(["card","carbon","carzone"]))




