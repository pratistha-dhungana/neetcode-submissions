class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}
        
        
        for index, value in enumerate(numbers):
            diff = target - value
            if diff not in seen:
                seen[value] = index
            else:
                return [seen[diff]+1, index+1]
        