class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for words in strs:
            clean = sorted(words)
            key = ",".join(clean)

            if key not in results:
                results[key] = [words]
            else:
                results[key].append(words)
        
        return list(results.values())