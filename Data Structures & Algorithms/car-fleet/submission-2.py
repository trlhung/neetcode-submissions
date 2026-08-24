class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = [(p, s) for p, s in zip(position, speed)]
        car.sort(reverse=True)

        stack = []

        for each in car:
            reaching_time = (target - each[0]) / each[1]
            
            if not stack or stack[-1] < reaching_time:
                stack.append(reaching_time)

        return len(stack)