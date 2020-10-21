class Solution(object):
    def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
        """
        sum = 0
        n = len(nums)
        print(n)
        total = (n + 1) * (n + 2) / 2
        for i in range(0, len(nums)):
            sum = sum + nums[i]

        missing_no = total - sum
        return missing_no

    nums = [1, 2, 4]
    a = missingNumber(nums)
    print(a)

