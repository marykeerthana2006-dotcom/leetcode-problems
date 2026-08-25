class Solution:
    def repeatedSubstringPattern(self, s):

        n = len(s)

        for i in range(1, n):

            if n % i == 0:

                substring = s[:i]

                if substring * (n // i) == s:
                    return True

        return False