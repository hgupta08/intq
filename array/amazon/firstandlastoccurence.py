# Python 3 program to find first and
# last occurrence of an elements in
# given sorted array


# Function for finding first and last
# occurrence of an elements
def findFirstAndLast(arr, n, x):
    first = -1
    last = -1
    for i in range(0, n):
        if (x != arr[i]):
            continue
        if (first == -1):
            print("in loop")
            first = i
            print(first)
        last = i
        print(last)

    if (first != -1):
        print("First Occurrence = ", first,
              " \nLast Occurrence = ", last)
    else:
        print("Not Found")

    # Driver code


arr = [1, 5, 3, 2, 2, 3, 4, 7]
n = len(arr)
x = 2
findFirstAndLast(arr, n, x)