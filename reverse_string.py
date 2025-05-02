def reverse_string(s):

    left, right = 0, len(s) - 1  # Initialize two pointers
    while left < right:
        # Swap the characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
        # Move the pointers closer to the center
        left += 1
        right -= 1

# Example usage
s = ['h', 'e', 'l', 'l', 'o']
reverse_string(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']