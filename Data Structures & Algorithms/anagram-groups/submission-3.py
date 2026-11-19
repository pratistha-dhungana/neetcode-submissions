class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for word in strs:
            word_sort = sorted(word)
            joined_words = ','.join(word_sort)
            

            if joined_words not in seen:
                seen[joined_words] = [word]
            else:
                seen[joined_words].append(word)
                
        return (list(seen.values()))
            