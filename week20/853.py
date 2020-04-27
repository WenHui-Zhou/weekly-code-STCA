class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        res = sorted(zip(position,speed))
        time = [(target - p)*1.0 / s for p,s in res]
        
        ans = 0
#        print(res)
        while len(time) > 1:
            lead = time.pop()
            if lead >= time[-1]:
            #    ans += 1
                time[-1] = lead
            else:
                ans += 1
        return ans + bool(time)
                
