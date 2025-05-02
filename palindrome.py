def is_palindrome(s: str) -> bool:
    # Preprocess the string to keep only alphanumeric characters and make them lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    print(filtered)
    # Check if the filtered string is equal to its reverse
    return filtered == filtered[::-1]

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))

# def palindrome(s):
#
#     if s == s[::-1]:
#         return True
#     return False
#
# print(palindrome("sos"))

# function to check string is
# palindrome or not
# def is_palindrome(s):
#
#     # Using predefined function to
#     # reverse to string print(s)
#     rev = ''.join(reversed(s))
#
#     # Checking if both string are
#     # equal or not
#     if (s == rev):
#         return True
#     return False


# def is_palindrome(s):
#     for i in range(0, int(len(s)/2)):
#         if s[i] != s[len(s)-i-1]:
#             return False
#     return True
#
# # main function
# s = "A man, a plan, a canal: Panama"
# ans = is_palindrome(s)
# print(ans)

# def is_palindrome(s: str) -> bool:
#     left, right = 0, len(s) - 1
#
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#
#     return True
#
# # Example usage
# print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(is_palindrome("hello"))    # Output: False