class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                count = dict1.get(s[i])
                count +=1
                dict1[s[i]] = count

        for j in range(len(t)):
            if t[j] not in dict2:
                dict2[t[j]] = 1
            else:
                count = dict2.get(t[j])
                count += 1
                dict2[t[j]] = count

        if dict1 == dict2:
            return True
        else: 
            return False
        