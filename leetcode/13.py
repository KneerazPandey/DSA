class Solution(object):
    def roman_to_int(self, data: str):
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        result = 0
        for i in range(len(data)):
            if i + 1 < len(data) and mapping[data[i]] < mapping[data[i + 1]]:
                result -= mapping[data[i]]
            else:
                result += mapping[data[i]]
                
        return result 
        
data = "MCMXCIV"
s = Solution()
print(s.roman_to_int(data))