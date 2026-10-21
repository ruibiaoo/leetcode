class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict1 = {}

        for num in nums:
            if num not in dict1:
                dict1[num] = 0
            dict1[num] +=1
        
        array = sorted(dict1.items(), key = lambda item: item[1], reverse = True)
        ans = []
        for key,value in array[:k]:
            ans.append(key)
        return ans

            

        