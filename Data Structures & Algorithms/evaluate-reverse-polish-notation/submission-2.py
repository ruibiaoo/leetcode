class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        stack = []
        operators = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                if len(stack) >= 2:
                    num1 = stack.pop(-1)
                    num2 = stack.pop(-1)
                else:
                    continue

                if t == "+":
                    total = num1 + num2
                elif t == "-":
                    total = num2 - num1
                elif t == "*":
                    total = num1 * num2
                else:
                    total = num2 / num1
                    if total < 0:
                        total = math.floor(abs(total)) * -1
                    else:
                        total = math.floor(total)
                stack.append(total)
        return stack[0]