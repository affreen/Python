"""demo - script that converts a number into an alphabet and then
determines whether it is an uppercase or lowercase vowel or consonant"""

print("Enter a digit:")
var=input()
var=int(var)

new_var=chr(var)
#if(new_var>=97 and new_var<=122):
if (new_var in ['a','e','i','o','u']):
    print("You have entered a lowercase vowel:", new_var)
elif(new_var in ['A','E','I','O','U']):
    print("You have entered an uppercase vowel:", new_var)
else:
    print("You have entered a consonant:", new_var)
