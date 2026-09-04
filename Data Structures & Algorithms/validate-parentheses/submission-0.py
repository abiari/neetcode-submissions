class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        brackets = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
                continue
            if not len(stack) or c != stack.pop():
                return False
        if len(stack):
            return False
        return True