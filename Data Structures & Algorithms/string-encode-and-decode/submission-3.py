class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            for c in s:
                encoded += f"{ord(c)} "
            encoded += "_ "
        return encoded.rstrip()
            

    def decode(self, s: str) -> List[str]:
        letters = s.split(' ')
        print(letters)
        decoded = []
        i = 0
        while i < len(letters):
            curr = ""
            char = letters[i]
            if len(char) != 0:
                while char != "_":
                    curr += chr(int(char))
                    i += 1
                    if i >= len(letters):
                        break
                    char = letters[i]
                decoded.append(curr)
            i += 1
        return decoded

