class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_str = sorted(s)
        t_str = sorted(t)
        if s_str != t_str:
            return False
        return True