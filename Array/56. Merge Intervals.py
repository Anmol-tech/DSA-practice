'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        intervals.sort()
        while i < len(intervals):
            groups = 1
            while (i + groups < len(intervals)
                   and intervals[groups + i][0] <= intervals[i][1]):
                intervals[i][0] = min(intervals[i][0], intervals[groups + i][0])
                intervals[i][1] = max(intervals[i][1], intervals[groups + i][1])
                groups += 1

            ans.append(intervals[i])
            i += groups

        return ans

'''
Time Complexity: O(nlogn)
Space Complexity: O(k)
'''

if __name__ == "__main__":
    input = [[1,4],[0,0]]
    print(Solution().merge(input))