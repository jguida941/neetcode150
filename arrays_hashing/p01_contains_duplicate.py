"""Contains Duplicate — Easy
https://neetcode.io/problems/duplicate-integer

Given an integer array nums, return true if any value appears more than
once in the array, otherwise return false.

Example 1:
    Input:  nums = [1, 2, 3, 3]
    Output: true

Example 2:
    Input:  nums = [1, 2, 3, 4]
    Output: false

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

Approach:
    (fill in after solving — one or two sentences on the key idea)

Complexity:
    Time:  O(?)
    Space: O(?)
"""


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Loop through the list using each value's index.
        # Example: nums = [1, 2, 3, 3]
        #
        # range() needs an integer that tells it when to stop.
        # len(nums) returns the number of values in the list.
        #
        # len(nums) = 4
        # range(4) generates the indexes: 0, 1, 2, 3
        for i in range(len(nums)):
            # Start j after i so we skip the current value and 
            # only check the values after it.
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        # If every comparison finishes with out a match
        # That means there are no duplicates 
        return False

