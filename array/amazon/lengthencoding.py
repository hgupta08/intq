def encode(message):
    encoded_message = ""
    i = 0

    while (i <= len(message) - 1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message) - 1):
            print(j)
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break

        encoded_message = encoded_message + ch+ str(count)
        print(encoded_message)
        print(ch)

        i = j + 1
    return encoded_message


# Provide different values for message and test your program
encoded_message = encode("ABBBBCCC")
print(encoded_message)