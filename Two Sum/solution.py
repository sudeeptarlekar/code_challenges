from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        diff = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if checked.get(diff) != None:
                return [checked.get(diff), i]
                break

            checked[nums[i]] = i
