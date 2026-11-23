class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        strings = ["+", "D", "C"]

        for v in operations:
            if v not in strings:
                stack.append(int(v))
            elif v == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                total = num1 + num2
                stack.append(total)
            elif v == "D":
                num1 = stack[-1]
                total = num1 * 2
                stack.append(total)
            else:
                stack.pop(-1)

        res = 0
        for num in stack:
            res += num
        return res
            
        