def shiftChars():
    """A simple function that shifts the characters based on Unicode code."""
    string = input('Enter a string and the characters will be shifted by 1. ')
    newList = [chr(ord(i) + 1) for i in string]
    string_adj = ''.join(newList)
    print(string_adj)
shiftChars()
