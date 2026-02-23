# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if stack:
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(ch)
            elif ch in "({[":
                stack.append(ch)
            else:
                return False
        
        return len(stack) == 0