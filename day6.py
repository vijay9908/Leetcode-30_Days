class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        temp = defaultdict(list)
        for ele in strs:
            temp[str(sorted(ele))].append(ele)
        return list(temp.values())
        