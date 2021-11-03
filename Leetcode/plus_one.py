# class Solution:
#    def plusOne(self, digits: List[int]) -> List[int]:
#        for idx in range(len(digits) - 1, -1, -1):
#            if digits[idx] != 9:
#                digits[idx] += 1
#                break
#            else:
#                digits[idx] = 0
#        if digits[0] == 0:
#            digits.insert(0, 1)
#        return digits


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        num = 0
        for d in digits:
            num *= 10
            num += d

        num += 1
        output = []

        while num:
            temp = num % 10
            num //= 10
            output.append(temp)

        return output[::-1]


if __name__ == '__main__':
    digits = input().strip()
    print(Solution.plusOne(digits))
