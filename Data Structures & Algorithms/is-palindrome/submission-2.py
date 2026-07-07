class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        return s_clean == s_clean[::-1]
        