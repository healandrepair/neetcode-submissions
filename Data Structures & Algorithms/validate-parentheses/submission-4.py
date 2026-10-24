class Solution:
    def isValid(self, s: str) -> bool:

        dictionary = {"]": "[", "}": "{", ")": "("}
        stack = []
        for element in s:
            if element not in dictionary:
                stack.append(element);
            else:
                if (stack):
                    value = stack.pop(-1)
                    if (dictionary[element] == value):
                        continue
                return False

        if (stack):
            return False

        return True  
        