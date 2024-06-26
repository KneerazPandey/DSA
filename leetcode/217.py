class Solution(object):
    def contains_duplicate(self, nums: list[int]) -> bool:
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True 
            hashset.add(num)
            
        return False
    

nums = [1,1,1,3,3,4,3,2,4,2]
s = Solution()
print(s.contains_duplicate(nums))