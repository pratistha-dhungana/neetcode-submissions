class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep track of the indices and the value in it

        seen = {} # have a dict so we can keep track of both indices + value

        for i in range(len(nums)):
            difference = target - nums[i]

            if nums[i] not in seen:
                seen[difference] = i 
            else:
                return[seen[nums[i]], i]


