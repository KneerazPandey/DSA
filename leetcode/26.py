class Solutions(object):
    def remove_duplicates(self, nums: list[int]) -> int:
        replacement_target = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[replacement_target] = nums[i]
                replacement_target += 1
                
        return replacement_target
    
    
    
s = Solutions()
nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
print(s.remove_duplicates(nums))
print(nums)