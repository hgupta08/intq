# Python program to check
# if a string is palindrome 
# or not

x = "fvg"

w = ""
for i in x:
    w = i + w
    print(w)


if (x == w):
    print("Yes")
else:
    print("No")