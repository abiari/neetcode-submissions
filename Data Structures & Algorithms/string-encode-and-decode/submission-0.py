class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for el in strs:
            encoded_string += str(len(el)) + '#' + el
        return encoded_string
    def decode(self, s: str) -> List[str]:
        substr_len = ""
        decoded_strs = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                substr = ""
                length = int(substr_len)
                i += 1
                for j in range(length):
                    substr += s[i + j]
                i += length
                decoded_strs.append(substr)
                substr_len = ""
                continue
            substr_len += s[i]
            i += 1
        return decoded_strs