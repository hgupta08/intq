# Python3 program to count distinct
# prime factors of a number
import math


# Function to count the number of distinct
# prime factors of product of array
def Distinct_Prime_factors(a):
    # use set to store distinct factors
    m = set()

    # iterate over every element of array
    for i in range(len(a)):
        sq = int(math.sqrt(a[i]))

        # from 2 to square root of number run
        # a loop and check the numbers which
        # are factors.
        print(sq)
        for j in range(2, sq + 1):
            print(a[i], j)

            if (a[i] % j == 0):

                # if j is a factor store
                # it in the set
                m.add(j)

                # divide the number with j till it
                # is divisible so that only prime
                # factors are stored
                while (a[i] % j == 0):
                    print(a[i],j)
                    a[i] //= j

                # if the number is still greater
        # than 1 then it is a prime factor,
        # insert in set
        if (a[i] > 2):
            m.add(a[i])

    print(m)

        # the number of unique prime factors
    # will the size of the set
    return len(m)


# Driver Code
if __name__ == "__main__":
    a = [10,12,7]
    print(Distinct_Prime_factors(a))

# This code is contributed by ita_c
