class Solution(object):
    def haystack_and_needle(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i 
            
        return -1
    
    
haystack = "sadbutsad"
needle = "sad"
s = Solution()
print(s.haystack_and_needle(haystack=haystack, needle=needle))