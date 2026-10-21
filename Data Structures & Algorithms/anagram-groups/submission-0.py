class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs == [""]:
            return [[""]]
        
        if len(strs) == 1:
            return [strs]
        
        dict1 = {}

        for s in strs:
            base = "".join(sorted(s))
            if base not in dict1.keys():
                dict1[base] = []
            dict1.get(base).append(s)
        
        ans =[]
        for arr in dict1.values():
            ans.append(arr)
        return ans

        

        