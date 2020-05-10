iclass Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people == []:
            return people
        people.sort(key = lambda x:(x[0],x[1]))
    #    print(people)
        for cur in range(len(people))[::-1]:
            same = 0
            tmp = cur
            while tmp > 0:
                if people[tmp][0] == people[tmp-1][0]:
                    same += 1
                    tmp -= 1
                else:
                    break
            more = people[cur][1] - same
            if more > 0:
                val = people.pop(cur)
                people.insert(cur+more,val)
        return people

