"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

nums = [2,7,11,15] 
target = 9


def find_two_sum(nums, target):
    length = len(nums) #this -1 gives you index num
    index_len = length - 1
    output = []
    output_index = []
    
    for index, value in enumerate(nums):
        output.append(value)
        output_index.append(index)
        total = sum(output)
        if total == target:
            print(output)
            print(output_index)
            break
        else:
            continue

find_two_sum(nums, target)
