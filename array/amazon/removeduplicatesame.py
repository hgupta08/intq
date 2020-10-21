def removeAdjDup(s, n):

    chars = list(s)

    # k maintains the index of next free location in the result
    k = 0

    # i maintains the current index in the String
    # start from the second character
    i = 1
    print(chars)
    while i < len(chars):

        # if current character is not same as the
        # previous character, add it to result
        if chars[i - 1] != chars[i]:
            print("in if loop")
            print(chars)
            chars[k] = chars[i - 1]
            k = k + 1
            print(chars)

        else:
            print("in else loop")
            # remove adjacent duplicates
            print(chars[i - 1],chars[i])
            while i < len(chars) and chars[i - 1] == chars[i]:
                i = i + 1

        i = i + 1


    print("chars at end of loop",chars)
    print(i,k)

    # Add last character to result
    chars[k] = chars[i - 1]
    k = k + 1

    print("chars",chars)


    # construct the with first k chars
    s = ''.join(chars[:k])

    print("combine s",s)

    # start again if any duplicate is removed
    if k != n:
        print("going again",s)
        return removeAdjDup(s, k)  # Shlemiel Painter's Algorithm

    # if the algorithm didn't change the input String, that means
    # all the adjacent duplicates are removed
    return s


if __name__ == '__main__':

    str = "DBCCA"
    print("The left after removal of all adjacent duplicates is",
          removeAdjDup(str, len(str)))
