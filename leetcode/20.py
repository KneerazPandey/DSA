class Solution(object):
    def valid_parenthesis(self, data):
        mapping = {
            ')': '(',
            '}': '{',
            ']': '[',
        } 
        stack = []
        for char in data:
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False  
            else:
                stack.append(char)
                
        return True if not stack else False
                
    
data = "()[]{}"
s = Solution()

print(s.valid_parenthesis(data=data)) 