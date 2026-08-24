class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        car = [[0, 0]] * n

        for i in range(n):
            car[i] = [position[i], speed[i]]
        
        car.sort(reverse=True)

        stack = []

        for each in car:
            reaching_time = (target - each[0]) / each[1]
            
            if not stack or stack[-1] < reaching_time:
                stack.append(reaching_time)

        return len(stack)