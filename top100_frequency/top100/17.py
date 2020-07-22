class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
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
        
        if digits == '':
            return []
        dig_to_char = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def get_nums(digits,ans,res,dig_to_char):
            if digits == '':
                ans.append(res)
                return
            for c in dig_to_char[int(digits[0]) -2]:
                get_nums(digits[1:],ans,res+c,dig_to_char)
        ans = []
        get_nums(digits,ans,'',dig_to_char)
        return ans"""
        if digits == '':
            return []
        dig_to_char = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def get_char(digits,dig_to_char,res,ans):
            if digits == '':
                ans.append(res)
                return
            for c in dig_to_char[int(digits[0]) - 2]:
                get_char(digits[1:],dig_to_char,res+c,ans)
        ans = []
        get_char(digits,dig_to_char,'',ans)
        return ans






