class Solution(object):
    def longest_common_prefix(self, datas: list[str]) -> str:
        if len(datas) <= 0: return ''
        
        first = datas[0]
        output = ''
        for i in range(len(first)):
            for item in datas:
                if i == len(item) or item[i] != first[i]:
                    return output
            
            output += first[i]
        
        return output
    
    
strs = ["flower","flow","flight"]
s = Solution()
print(s.longest_common_prefix(strs))