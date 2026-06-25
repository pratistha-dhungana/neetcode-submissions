class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen ={}
        t_seen = {}

        for char in s:
            if char not in s_seen:
                s_seen[char] = 1
            else:
                s_seen[char] += 1
        
        for char in t:
            if char not in t_seen:
                t_seen[char] = 1 
            else:
                t_seen[char] += 1
        
        return s_seen == t_seen