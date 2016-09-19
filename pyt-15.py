"""demo - while loop that keeps on executing if the user has input an
even number and breaks if the user enters an odd number"""



while True:
    print("Enter a number of your choice:")
    var=input()
    var=int(var)
    if(var%2==1):
        break
print("You have an odd number!")
        
