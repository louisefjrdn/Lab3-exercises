
def reverseRecursion(given_string):
    stringLen = len(given_string)

    if stringLen == 1:
        return given_string
    else:
        return reverseRecursion(given_string[1:]) + given_string[0]

givenstring = 'papasa every sem'
print('The modified given string{after reversing} = ',
      reverseRecursion(givenstring))
print(givenstring.replace('s', ''))

