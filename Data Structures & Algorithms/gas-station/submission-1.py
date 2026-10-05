class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

#gas[result]=x, gas[result+1]=x-cost[result]+gas[result+1], 
#gas[result+2]=x-cost[result]+gas[result+1]-cost[result+1]+gas[result+2]
        if sum(gas)<sum(cost):
            return -1
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:         # can't get from `start` past station i
                start = i + 1    # so no station from start..i works, try the next one
                tank = 0
        return start