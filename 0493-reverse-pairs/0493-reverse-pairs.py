class Solution:
    def reversePairs(self, nums):
        def merge(l, r):
            if l >= r:
                return 0

            m = (l + r) // 2
            count = merge(l, m) + merge(m + 1, r)

            j = m + 1
            for i in range(l, m + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - m - 1

            nums[l:r+1] = sorted(nums[l:r+1])
            return count

        return merge(0, len(nums) - 1)