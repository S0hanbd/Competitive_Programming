class Solution(object):
    def removeElement(self, nums, val):
        loc =0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[loc] = nums[i]
                loc +=1
        return (loc)