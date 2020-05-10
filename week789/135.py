class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        
        left  = [1]*len(ratings)
        right = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for i in range(len(ratings) - 1)[::-1]:
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        res = []
        for i in range(len(left)):
            res.append(max(left[i],right[i]))
        return sum(res)
        """
        left = [1]*len(ratings)
        right = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for j in range(len(ratings)-1)[::-1]:
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1] + 1
        res = []
        for i in range(len(ratings)):
            res.append(max(left[i],right[i]))
        return sum(res)

