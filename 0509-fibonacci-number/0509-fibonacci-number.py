class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev, curr = 0, 1
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr