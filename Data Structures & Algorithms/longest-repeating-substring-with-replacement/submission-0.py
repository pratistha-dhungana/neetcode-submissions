class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] not in seen:
                seen[s[right]] = 1
            else:
                seen[s[right]] += 1
            
            
            
            while (right-left + 1)- max(seen.values()) > k:
                seen[s[left]]-=1
                left +=1
            
            win_length = right-left + 1

            if win_length > result:
                result = win_length
        return result