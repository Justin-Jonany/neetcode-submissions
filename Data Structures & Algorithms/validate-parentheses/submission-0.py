class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pair = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for char in s:
            # print(stack)
            if len(stack) > 0 and stack[-1] == bracket_pair.get(char, ''): # if it's an open bracket we don't remove anything from stack
                stack.pop()
                # print(f'popped: {stack}')
            else:
                stack.append(char)
        return True if len(stack) == 0 else False
