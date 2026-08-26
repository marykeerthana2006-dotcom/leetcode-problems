class Solution:
    def longestDupSubstring(self, s):
        n = len(s)

        base = 26
        mod = 10**9 + 7

        nums = [ord(c) - ord('a') for c in s]

        def check(length):
            if length == 0:
                return ""

            power = pow(base, length - 1, mod)

            h = 0

            for i in range(length):
                h = (h * base + nums[i]) % mod

            seen = {h}

            for i in range(length, n):
                h = (
                    (h - nums[i - length] * power) * base
                    + nums[i]
                ) % mod

                if h in seen:
                    # Verify to avoid hash collision
                    start = i - length + 1
                    candidate = s[start:start + length]

                    for j in range(start):
                        if s[j:j + length] == candidate:
                            return candidate

                seen.add(h)

            return None

        left = 1
        right = n - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2

            result = check(mid)

            if result is not None:
                answer = result
                left = mid + 1
            else:
                right = mid - 1

        return answer