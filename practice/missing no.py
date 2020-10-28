class Solution(object):
    def findDisappearedNumbers(nums):
        #a = set(i for i in range(1, len(nums) + 1))
        b = set(nums)
        a=set()
        for i in range(1,len(nums)+1):
            print(i)
            a.add(i)

            #a=set(i)
        print(a)
        print(b)

        return list(a - b)


    print(findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1]))
