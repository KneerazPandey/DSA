from typing import List

class Solution(object):
    def contains_duplidate(self, nums: List[int]) -> bool:
        #? Time Complexity: O(n^2)
        #? Space Complexity: O(1)
        for i in range(len(nums)):
            for j in range(i, len(nums) - 1):
                if nums[i] == nums[j]:
                    return True
                
        return False
    
    def contains_duplicate(self, nums: List[int]) -> bool:
        #? Time Complexity: O(n)
        #? Space Complexity: O(n)
        
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True 
            hashset.add(num)
            
        return False
    

nums = [1,1,1,3,3,4,3,2,4,2]
s = Solution()
print(s.contains_duplicate(nums))