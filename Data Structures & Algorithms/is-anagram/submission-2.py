class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seen = {}
        seen_t = {}

        for chars in s:
            if chars not in seen:
                seen[chars] = 1
            else:
                seen[chars] += 1

        for chars in t :
            if chars not in seen_t:
                seen_t[chars] = 1
            else:
                seen_t[chars] += 1
        
        return seen == seen_t