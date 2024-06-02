class Solution(object):
    def remove_element(self, nums, val):
        changable = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[changable] = nums[i]
                changable += 1
                
        return changable
    

nums = [0,1,2,2,3,0,4,2]
val = 2

s = Solution()
print(s.remove_element(nums=nums, val=val))