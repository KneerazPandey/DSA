from typing import List


class Solution(object):
    def find_disappeared_number(self, nums: List[int]) -> List[int]:
        #? Time Complexity: O(n)
        #? Space Complexity: O(n)
        if len(nums) == 0:
            return []
        expected_set = set(range(1, len(nums) + 1))
        actual_set = set(nums)
        return list(expected_set - actual_set)
    
    def find_disappeared_number(self, nums: List[int]) -> List[int]:
        #? Time Complexity: O(n)
        #? Space Complexity: O(n)
        nums_set = set(nums)
        output = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                output.append(i)
                
        return output
    
    def find_disappeared_number(self, nums: List[int]) -> List[int]:
        #? Time Complexity: O(n) + O(n) == O(n)
        #? Space Complexity: O(1) 
        #! Worst case senerio -> Space Complexity: O(n)
        output = []
        if len(nums) == 0:
            return output
        
        for i in range(len(nums)): 
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] = nums[temp] * -1
                
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i + 1)
            else:
                nums[i] = nums[i] * -1
                
        return output 
        
        
    
sol = Solution()
nums = [4,3,2,7,8,2,3,1]
output = sol.find_disappeared_number(nums)
print(output)