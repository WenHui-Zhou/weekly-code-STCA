class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        goal = 0
        cur = 0
        pos = -1
        for ii in range(len(gas)):
            goal += gas[ii] - cost[ii]    
            cur += gas[ii] - cost[ii]
            if cur < 0:
                cur = 0
                pos = -1
            else:
                if pos == -1:
                    pos = ii
        if goal >= 0:
            return pos
        else:
            return -1