# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l == r:
        print("l=r")

        print(toString(a))
    else:
        for i in range(l, r + 1):
            print("swap",a[l],a[i])
            print("l,r",l,r)
            print("i",i)
            print("**************************")




            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)

            print("finalll....")
            print("swap",a[l],a[i])


            a[l], a[i] = a[i], a[l]  # backtrack
            print("end of loop....")



# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)









