class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket is '(' or bracket is '{' or bracket is '[':
                stack.append(bracket)
            elif (bracket is ')' or bracket is '}' or bracket is ']') and stack != []:
                if bracket is ')' and stack.pop() != '(':
                    return False
                elif bracket is '}' and stack.pop() != '{':
                    return False
                elif bracket is ']' and stack.pop() != '[':
                    return False
            else:
                return False
        return stack == []