class Solution(object):
    def length_of_last_word(self, words):
        length = 0
        index = len(words) - 1
        
        while words[index] == " ":
            index -= 1
            
        while index >= 0 and words[index] != " ":
            length += 1
            index -= 1
            
        return length
    
    
words = "Hello World"
s = Solution()
print(s.length_of_last_word(words=words)) 