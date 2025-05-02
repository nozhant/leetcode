class MyAtoi:

    def my_atoi(self, s: str) -> int:
        s = s.lstrip()  # Step 1: Remove leading whitespace
        if not s:
            return 0

        sign = 1
        i = 0

        # Step 2: Handle optional sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        result = 0

        # Step 3: Convert digits and skip leading zeros
        while i < len(s) and s[i] == '0':
            print(s[i])
            i += 1  # skip leading zeros

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Step 4: Clamp to 32-bit signed int range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result

instance = MyAtoi()
print(instance.my_atoi("-00042"))