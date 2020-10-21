# Python3 program to remove consecutive
# duplicates from a given string.

# A iterative function that removes
# consecutive duplicates from string S
def removeDuplicates(S):
    n = len(S)

    # We don't need to do anything for
    # empty or single character string.
    if (n < 2):
        return

    # j is used to store index is result
    # string (or index of current distinct
    # character)
    j = 0

    # Traversing string
    for i in range(n):

        # If current character S[i]
        # is different from S[j]
        print("comparing ",S[j],S[i])
        print("i and j ",i,j)

        if (S[j] != S[i]):
            j += 1
            print("equating ", S[j], S[i])

            S[j] = S[i]
            print("Inside loop",S)
        print("outside",S)

        # Putting string termination
    # character.
    print("AAA", S[:j])

    j += 1
    S = S[:j]
    return S


# Driver Code
if __name__ == '__main__':
    S1 = "abbccc"
    S1 = list(S1.rstrip())
    S1 = removeDuplicates(S1)
    print(S1, sep="")


# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
