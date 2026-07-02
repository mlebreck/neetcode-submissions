class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for c in s:
            if c.isalpha() or c.isdigit():
                string += c.lower()

        return string[::-1] == string
