class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        k = 0
        for c in s:
            if k < len(t) and c == t[k]:
                k += 1
        return len(t) - k