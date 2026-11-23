class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []

        for letter in s:
            if letter in dict1.values():
                stack.append(letter)
            elif letter in dict1.keys():
                if len(stack) == 0:
                    return False
                existing = stack.pop(-1)
                if dict1.get(letter) != existing:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

        