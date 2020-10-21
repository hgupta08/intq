class Solution(object):
    def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

        """
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            print(nums[i])
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(current_sum, max_sum)

        return max_sum

    if __name__ == "__main__":
        arr = [0, 2, -2, -20, 10]
        n = len(arr)
        Sum = 10

        a=maxSubArray(arr)
        print(a)

