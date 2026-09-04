class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n_cars = len(position)
        n_fleets = 1
        lane = []
        for i in range(n_cars):
            lane.append((position[i], speed[i]))
        lane = sorted(lane, key=lambda x: x[0])
        lane.reverse()
        fleetETA = (target - lane[0][0]) / lane[0][1]
        for i in range(1, n_cars):
            currentCarETA = (target - lane[i][0]) / lane[i][1]
            if currentCarETA > fleetETA:
                n_fleets += 1
                fleetETA = currentCarETA

        return n_fleets