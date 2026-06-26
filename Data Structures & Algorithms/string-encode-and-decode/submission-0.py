class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for items in strs:
            encoded_string += str(len(items)) + '#' + items
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        position = 0

        while position < len(s):
            ind = s.find('#', position)
            length = int(s[position:ind])

            word_start = ind + 1
            word_end = word_start + length

            word = s[word_start:word_end]
            result.append(word)
            position = word_end 

        return result 
