class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        OPERATORS = ['+', '-', '*', '/']
        numbers = []
        for token in tokens:
            # print(f'{numbers}:    {token}')
            if token not in OPERATORS:
                numbers.append(token)
            else: # take two and apply the operator
                second = int(numbers.pop())
                first = int(numbers.pop())
                if token == '+':
                    result = (first + second)
                elif token == '-':
                    result = (first - second)
                elif token == '*':
                    result = (first * second)
                elif token == '/':
                    result = int(first / second)
                numbers.append(result)
        return numbers[0]
            
