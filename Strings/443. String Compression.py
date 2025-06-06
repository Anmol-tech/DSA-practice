'''
443. String Compression
Medium
Topics
Companies
Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


Constraints:
1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
'''
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_idx = 0
        res = 0
        while curr_idx < len(chars):
            group_length = 1
            while (
                curr_idx + group_length < len(chars)
                and chars[group_length + curr_idx] == chars[curr_idx]
            ):
                group_length += 1

            chars[res] = chars[curr_idx]
            res += 1

            if group_length > 1:
                group_length = str(group_length)
                chars[res:res+len(group_length)] = list(group_length)
                res += len(group_length)

        return res

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

if __name__=="__main__":
   sol = Solution()
   chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
   print(sol.compress(chars))
   print(chars)