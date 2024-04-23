class Solution(object):
    def is_palindrome(self, num: int) -> bool:
        num_str = str(num)
        return num_str == num_str[::-1]
    
    def is_palindrome(self, num: int) -> bool:
        #* Time Complexity: O(n)
        #* Space Complexity: O(1)
        if num < 0: return False 
        div = 1
        while div * 10 <= num:
            div *= 10
            
        while num:
            right = num % 10
            left = num // div 
            
            if (right != left): return False 
            
            num = (num % div) // 10
            div = div / 100

        return True
        
    
    

x = 121
s = Solution()
print(s.is_palindrome(x))
