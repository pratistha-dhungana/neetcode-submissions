class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1
        
        sorted_result = sorted(result, key=result.get, reverse=True)
        return(sorted_result[:k])
