class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if not stk:
                stk.append(ch)
            elif stk[-1] == '(' and ch == ')':
                stk.pop()
            elif stk[-1] == '{' and ch == '}':
                stk.pop()
            elif stk[-1] == '[' and ch == ']':
                stk.pop()
            else:
                stk.append(ch)
        if not stk:
            return True
        return False