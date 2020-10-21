class Solution(object):
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count = count + 1

            else:
                count = count - 1
        return candidate


    arr=[2,3,4,3,3]
    a=majorityElement(arr)
    print(a)