class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = [0] * 128
        for c in s:
            char_count[ord(c)] += 1

        s = sorted(s, key=lambda c: (-char_count[ord(c)], c))
        return ''.join(s)