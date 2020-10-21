fname = input("Enter file name: ")

num_words = 0
no_of_line=0
characters=0
dt=dict()

with open(fname, 'r') as f:
    for line in f:
        no_of_line=no_of_line+1
        words = line.split(" ")
        num_words += len(words)
        for word in words:
            if word in dt:
                dt[word] += 1
            else:
                dt[word] = 1
            characters=characters+len(words)

        #characters += sum(len(word) for word in words)


print("Number of words:")
print(num_words)
print(no_of_line)
print(characters)
for key,value in dt.items():
    print(key,value)