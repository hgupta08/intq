    # python3 program to reverse individual words
    # in a given string using stl list

    # reverses individual words of a string
def reverserwords(string):
    st = list()

    # traverse given string and push all characters
    # to stack until we see a space.
    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])


        # when we see a space, we print
        # contents of stack.
        else:
            while len(st) > 0:
                print(st[-1], end= "")
                st.pop()

            print(end = " ")

    # since there may not be space after
    # last word.
    #while len(st) > 0:
    #    print(st[-1], end = "")
    #    st.pop()

    # driver code
if __name__ == "__main__":
    string = "geeks for geeks"
    reverserwords(string)

    # this code is contributed by
    # sanjeev2552
