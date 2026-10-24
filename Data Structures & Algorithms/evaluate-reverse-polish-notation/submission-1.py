class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = set(["+", "-", "*", "/"])
        stack = []
        i = 0
        n =len(tokens)
        while i < n:
            print(i)
            if (tokens[i] in operator):
                print(tokens[i])
                val2 = int(stack.pop(-1))
                val1 = int(stack.pop(-1))
                total = 0
                if (tokens[i] == "+"):
                    total = val1 + val2
                elif (tokens[i] == "-"):
                    total = val1 - val2
                elif (tokens[i] == "*"):
                    total = val1 * val2
                elif (tokens[i] == "/"):
                    total = val1 / val2
                
                stack.append(total)
            else:
                stack.append(tokens[i])

            print(stack)
            i += 1
        print(stack)
        return int(stack[0])