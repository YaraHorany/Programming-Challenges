# Given two strings first and second, consider occurrences in some text of the form "first second third", 
# where second comes immediately after first, and third comes immediately after second.

# Return an array of all the words third for each occurrence of "first second third".

def findOcurrences(text, first, second):
    arr = text.split(' ')
    output = list()

    for i in range(len(arr) - 2):
        if arr[i] == first and arr[i+1] == second:
            output.append(arr[i+2])

    return output


print(findOcurrences("alice is a good girl she is a good student", "a", "good")) # expected output: ["girl",student"]
print(findOcurrences("alice is aa good girl she is a good student", "a", "good", )) # expected output: ["student"]
print(findOcurrences("jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa", "kcyxdfnoa", "jkypmsxd")) # expected output: ['kcyxdfnoa', 'kcyxdfnoa', 'kcyxdfnoa']
print(findOcurrences("we we we we will rock you", "we", "we")) # expected output: ["we","we","will"]