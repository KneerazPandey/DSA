class Solution(object):
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        #* Time Complexity:- O(n^2)
        #* Space Complexity:- O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return [] 
    
    
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        #* Time Complexity:- O(n)
        #* Space Complexity:- O(n)
        memo = {}
        for i in range(len(nums)):
            res = target - nums[i] 
            if res in memo:
                return [memo[res], i]
            else:
                memo[nums[i]] = i 
            
        return []
    
    

nums = [2,7,11,15]
target = 9
s = Solution()

print(s.two_sum(nums, target))