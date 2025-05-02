class Solution:
    def strStr(haystack: str, needle: str) -> int:
        if not needle:
            return 0  # Empty string is always found at index 0

        len_h = len(haystack)
        len_n = len(needle)

        for i in range(len_h - len_n + 1):  # Only go up to where needle could fully fit
            print(i)
            if haystack[i:i + len_n] == needle:  # Compare substring of same length
                return i  # Found a match

        return -1  # No match found

print(Solution.strStr("hello", 'll'))








