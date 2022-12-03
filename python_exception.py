a=int(input('enter a value:'))
b=int(input('enter b value:'))

try:
    print("resource open")
    c=a/b
    print('Ans is :', c)
    d=int(input("Enter number:"))
    print(d)

##except Exception as error: # It detects every  error and print type of error
    ##print("An error has occured",error)

 
# except ZeroDivisionError: # This is to get the exact error which it belongs i.e. it detects zero division error only
#     print("An error has occured")

# except ValueError as e:# This is to get the exact error which it belongs i.e. it detects value error
#     print("you have not entered numeric value:  ", e)    

finally:
    print("resource closed")    