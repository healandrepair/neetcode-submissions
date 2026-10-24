class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        cars = sorted(zip(position, speed), reverse=True)
        print(cars)
        
        for pos, s in cars:
            timeSpentToTarget =(target - pos) / s
            print(timeSpentToTarget)
            time.append(timeSpentToTarget)

        last_time = 0
        res = 0
        for i in time:
            if i > last_time:
                last_time = i
                res += 1
            
        return res