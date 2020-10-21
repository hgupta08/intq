def reverse(s):
    str = ""
    for i in s:
        str = i + str
        print("value of i",i)
        print("value of str",str)
        print("*****")

    return str


s = "Geeks for geeks"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))