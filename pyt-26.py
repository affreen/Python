"""calculate the summation of  the numbers defined in a range"""

print("Enter 2 numbers:")
var1=input()
var1=int(var1)
var2=input()
var2=int(var2)

a=range(var1,var2)
b=sum(a)
print(b)
