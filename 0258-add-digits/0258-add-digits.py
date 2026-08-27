class Solution(object):
    def addDigits(self, num):

        while num >= 10:
            total = 0

            while num > 0:
                total = total + (num % 10)
                num = num // 10

            num = total

        return num