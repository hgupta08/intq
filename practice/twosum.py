def twosum(arr,target):


    dm={}

    for i in range(0,len(arr)):
        val=target-arr[i]
        if val in dm:
            print("sum of",arr[i],str(val))
            return True
        else:
            dm[arr[i]]=i






a = twosum(arr=[2, 3, 7, 9], target=10)
print(a)
