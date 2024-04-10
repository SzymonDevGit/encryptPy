import math

# Variables
inputUser = 'Default Input;'
outputTest = 'Default Output;'

workingArray = []
workingStep1 = []
workingStep2 = []

# Plain Text To Encrypted
def PTE (text):
    for i in range(len(text)):
        workingArray.append(ord(text[i]))

    for i in range(len(workingArray)):
        workingStep1.append(chr(((int(workingArray[i])+i)*2)-(23+i)))

    outputTest.join(workingStep1)

# Encrypted To Plain Text
def ETP (text):
    for i in range(len(text)):
        workingArray.append(ord(text[i]))

    for i in range(len(workingArray)):
        try:
            workingStep2.append(chr((int(workingArray[i])+(23+i))/2)-i)
        except:
            print(workingStep2)
            print(i)
            print(workingArray)

# Main Working Code
inputUser = input('Users/Python: ')

PTE(inputUser)
ETP(inputUser)
print(workingArray)
print(workingStep1)
print(''.join(workingStep1))
print(''.join(workingStep2))


