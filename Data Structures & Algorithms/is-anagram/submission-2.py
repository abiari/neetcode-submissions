class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = ''.join(sorted(s))
        tSorted = ''.join(sorted(t))
        
        if sSorted == tSorted:
            return True
        return False