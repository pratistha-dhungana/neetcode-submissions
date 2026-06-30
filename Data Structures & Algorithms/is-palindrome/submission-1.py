class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_clean = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        s_opp = s_clean[::-1]
        return s_clean==s_opp
        