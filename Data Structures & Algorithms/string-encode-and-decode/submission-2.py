class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for words in strs:
            encoded_string += str(len(words)) + '#' + words
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            
            find_i = s.find('#', i)
            find_len = s[i:find_i]
            str_to_len = int(find_len)

            start = find_i+1

            end = start + str_to_len
            word = s[start:end]
            
            result.append(word)
            start = end 
            i = start
        return result
        
            
        
