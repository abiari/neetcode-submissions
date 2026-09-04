class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_s = "".join([c.lower() for c in s if c.isalnum()])
        start = 0
        end = len(alphanum_s) - 1
        print(alphanum_s)
        while end > 0:
            if alphanum_s[start] != alphanum_s[end]:
                return False
            start += 1
            end -= 1
        return True