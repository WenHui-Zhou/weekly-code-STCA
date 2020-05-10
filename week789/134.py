class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        
        total_rank = 0
        cur_rank = 0
        start = 0
        for i in range(len(gas)):
            total_rank += gas[i] - cost[i]
            cur_rank += gas[i] - cost[i]
            if cur_rank < 0:
                cur_rank = 0
                start = i+1
        return start if total_rank >= 0 else -1
        """
        gas_cost = []
        for i in range(len(gas)):
            gas_cost.append(gas[i] - cost[i])
        if sum(gas_cost) < 0:
            return -1
        gas_cost += gas_cost
        lens = len(gas)
        c_gas = 0
        real = 0
        for cur in range(lens*2):
            c_gas += gas_cost[cur]
            if c_gas < 0:
                real = 0
                c_gas = 0
            else:
                real += 1
            if real == lens:
                return cur - lens + 1
        return -1

