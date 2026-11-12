class Solution:
    def insert(self, intervals, newInterval):
        res = []
        i, n = 0, len(intervals)

        # phase 1: intervals that end before the new one starts: copy unchanged
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # phase 2: intervals that overlap the new one: absorb them into it
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]),
                           max(newInterval[1], intervals[i][1])]
            i += 1
        res.append(newInterval)                          # append AFTER absorbing, not inside the loop

        # phase 3: intervals that start after the new one ends: copy unchanged
        while i < n:
            res.append(intervals[i])
            i += 1
        return res