# demo to check whether a letter is a vowel or consonant

print("Enter a letter:")
char=input()
char=str(char)

if(ord(char)>=65 and ord(char)<=90):
    if(char in ['A','E','I','O','U']):
       print("you have entered an uppercase letter!")
    else:
        print("you have entered a uppercase consonant!")
elif(ord(char)>=97 and ord(char)<=122):
    if(char in ['a','e','i','o','u']):
       print("you have entered a lowercase letter!")
    else:
        print("you have entered a lowercase consonant!")
else:
    print("This is not a letter!")
