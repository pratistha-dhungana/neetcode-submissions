class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        for number in nums:
            if number not in counter:
                counter[number] = 1
            else:
                counter[number] += 1
        
        sorted_counter = sorted(counter, key=counter.get, reverse = True)

        return sorted_counter[:k]
        