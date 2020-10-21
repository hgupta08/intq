# Function calling
def dictionairy():


    # Declare hash function
    key_value = {}

    # Initializing value
    key_value[2] = 'A'
    key_value[1] = 'C'
    key_value[3] = 'B'

    print("Task 1:-\n")
    print("Keys are")

    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for key,value in sorted(key_value.items()):
        print(key,value)
    for i in sorted(key_value.values()):
        print(i, end=" ")


def main():
    # function calling
    dictionairy()


# Main function calling
if __name__ == "__main__":
    main()
