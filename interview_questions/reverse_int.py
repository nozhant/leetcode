def reverse(x: int) -> int:
    # Define the 32-bit integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Determine the sign of x
    sign = -1 if x < 0 else 1

    # Reverse the absolute value of x
    reversed_num = int(str(abs(x))[::-1])

    # Restore the sign
    reversed_num *= sign

    # Check if the reversed number is within the 32-bit range
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0

    return reversed_num

# Example usage
print(reverse(123))    # Output: 321
print(reverse(-123))   # Output: -321
print(reverse(120))    # Output: 21
print(reverse(0))      # Output: 0
print(reverse(1534236469))  # Output: 0 (overflow case)
