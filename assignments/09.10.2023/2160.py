class Solution:
    def minimumSum(self, num: int) -> int:
        num_str = str(num)
        sorted_digits = sorted(num_str)
        new1 = ""
        new2 = ""
        if sorted_digits[0] == '0':
            new1 += sorted_digits[0]
            sorted_digits.pop(0)
        for i, digit in enumerate(sorted_digits):
            if i % 2 == 0:
                new1 += digit
            else:
                new2 += digit
        new1 = int(new1)
        new2 = int(new2)
        total_sum = new1 + new2

        return total_sum
    