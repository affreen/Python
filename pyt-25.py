"""script that calculates the summation of the numbers
(preceding the input number) that has been
typed in"""

print("Enter a number:")
var=input()
var=int(var)
a=range(var)
b=sum(a)
print(b)
