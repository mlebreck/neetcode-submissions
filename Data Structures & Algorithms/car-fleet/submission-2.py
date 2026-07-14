class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pairs, reverse=True):
            time = (target - p) / s
            while not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
