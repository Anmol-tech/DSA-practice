'''You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
'''
from typing import List



class SolutionDP:
    """
        DP and memorization
        TC: O(n^2)
        SC: O(n)
    """
    def jump(self, nums: List[int]) -> int:
        jumps = [0] * len(nums)
        return self.minimum_jumps(nums, 0, jumps)

    def minimum_jumps(self, nums, idx, jumps):
        if idx >= len(nums) - 1:
            return 0

        if jumps[idx] > 0:
            return jumps[idx]
        minimum_jump = float('inf')
        valid_jumps = nums[idx]
        while valid_jumps > 0:
            jump = self.minimum_jumps(nums, idx + valid_jumps, jumps)
            minimum_jump = min(minimum_jump, jump)
            valid_jumps -= 1
        jumps[idx] = minimum_jump + 1
        return minimum_jump + 1


class SolutionGreedy:
    """
    Greedy approach cover max area always
    TC: O(n)
    SC: O(1)
    """
    def jump(self, nums: List[int]) -> int:
        max_jump = i = last_jump = 0
        jump = 0
        for idx, num in enumerate(nums[:-1]):
            max_jump = max(max_jump, idx + num)
            if idx == last_jump:
                jump += 1
                last_jump = max_jump

        return jump
