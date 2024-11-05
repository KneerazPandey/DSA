from typing import List


class Solution(object):
    def missing_number(self, nums: List[int]) -> int:
        #? Time Complexity: O(n^2)
        #? Space Complexity: O(1)
        length = len(nums)
        for i in range(length):
            if i not in nums:
                return i 
            
    def missing_number(self, nums: List[int]) -> int:
        #? Time Complexity: O(n log n) + O(n) == O(n log n)
        #? Space Complexity: O(1)
        nums.sort()
        for index, num in enumerate(nums):
            if index != num:
                return index
            
            if len(nums) - 1 == num:
                return num + 1
            
    def missing_number(self, nums: List[int]) -> int:
        #? Time Complexity: O(n) + O(n) = O(n)
        #? Space Complexity: O(1)
        expected_sum = sum(range(0, len(nums) + 1))
        actual_sum = sum(nums)
        return expected_sum - actual_sum
            

sol = Solution()
nums = [8,6,4,2,3,5,7,0,1] # [0, 1, 2, 3, 4, 5, 6, 7, 8]
output = sol.missing_number(nums)
print(output) 