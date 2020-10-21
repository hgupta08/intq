class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.


        """

        index = 1

        while index < len(nums):
            if nums[index] == nums[index - 1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)
