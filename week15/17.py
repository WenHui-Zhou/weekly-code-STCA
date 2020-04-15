class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        dig_to_char = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def dfs(digits,dig_to_char,res,ans):
            if digits == '':
                ans.append(res[::])
                return
            for i in range(len(dig_to_char[int(digits[0]) - 2])):
                dfs(digits[1:],dig_to_char,res + dig_to_char[int(digits[0]) - 2][i],ans)
        ans = []
        dfs(digits,dig_to_char,'',ans)
        return ans
