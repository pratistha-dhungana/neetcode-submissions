class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, value in enumerate(nums):
            difference = target - value

            if difference not in result:
                result[value] = index
            else:
                return [result[difference], index]