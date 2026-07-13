class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []                                   # indices of days awaiting a warmer day

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()                      # this waiting day is now answered
                res[j] = i - j                       # how long it waited
            stack.append(i)                          # today is now waiting too

        return res