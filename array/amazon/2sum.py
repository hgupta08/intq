class Solution(object):
    def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_of_x = {}
        len_of_nums = len(nums)
        i = 0
        while i < len_of_nums:
            val = target - nums[i]
            print(dict_of_x)
            if (val in dict_of_x):
                print("Pair with given sum  is " ,str(nums[i]) + ", " + str(val))

                return [dict_of_x[val], i]
            dict_of_x[nums[i]] = i
            i += 1

    a=twoSum(nums=[2,3,7,9],target=9)
    print(a)
