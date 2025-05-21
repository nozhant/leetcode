class Solution:

    def plus_one(self, digits):

        result = 0
        for i in range(len(digits)):

            result = result*10 + int(digits[i])

        return [int(d) for d in str(result+1)]

    def plus_one_inplace(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits






