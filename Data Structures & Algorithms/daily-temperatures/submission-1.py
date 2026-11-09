class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temperature:
                popped_i, popped_temperature = stack.pop()
                days[popped_i] =  i - popped_i

            stack.append((i, temperature))
        return days

