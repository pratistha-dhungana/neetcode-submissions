class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}

        for ind, value in enumerate(numbers):
            difference = target - value

            if difference not in seen:
                seen[value] = ind
            else:
                return[seen[difference]+1, ind+1]
        