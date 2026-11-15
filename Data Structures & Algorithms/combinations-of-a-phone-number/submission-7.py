class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToC = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        def back(i, s):
            if i == len(digits):
                res.append(s[::])
                return
            
            for c in digitToC[digits[i]]:
                back(i + 1, s + c)
            
        if digits:
            back(0, "")
        return res