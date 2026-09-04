class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            count = [0] * 26
            if ''.join(sorted(s)) in seen:
                seen[''.join(sorted(s))].append(s)
                continue
            seen[''.join(sorted(s))] = [s]
        return list(seen.values())
        