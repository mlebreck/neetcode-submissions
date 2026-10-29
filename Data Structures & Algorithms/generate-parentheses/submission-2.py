class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def back(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                back(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(')')
                back(openN, closedN + 1)
                stack.pop()
        back(0, 0)
        return res