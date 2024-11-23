import string

def remove_punctuation(input_string):
    # Get the set of punctuation characters
    punctuations = set(string.punctuation)

    # Remove punctuations from the input string
    result_string = ''.join(char for char in input_string if char not in punctuations)

    return result_string

if __name__ == "__main__":
    input_string = input("Enter a string with punctuations: ")

    result = remove_punctuation(input_string)

    print("String without punctuations:", result)