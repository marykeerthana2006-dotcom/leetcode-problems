class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """

        k = 0
        repeated_word = ""

        while (repeated_word + word) in sequence:
            repeated_word += word
            k += 1

        return k