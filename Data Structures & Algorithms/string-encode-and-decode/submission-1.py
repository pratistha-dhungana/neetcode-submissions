class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for items in strs:
            encoded_string += str(len(items)) + '#' + items
        return encoded_string
    def decode(self, s: str) -> List[str]:
        result = []
        start_position = 0 

        while start_position < len(s):
            find_hashtag = s.find('#', start_position)
            find_length = int(s[start_position:find_hashtag])

            start_word_ind = find_hashtag + 1 
            end_word_ind = find_length + start_word_ind

            word = s[start_word_ind:end_word_ind]
            result.append(word)

            start_position = end_word_ind
        return result
