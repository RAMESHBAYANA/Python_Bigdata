# a=10
# def local_global_vr():
#     a=5
#     print("local variable:", a)

# local_global_vr()
# print("outside variable :", a)



# a=10
# def local_global_vr():   # making local to global variable: both cmd prints 5 here
#     global a
#     a=5
#     print("local variable:", a)

# local_global_vr() #prints 5
# print("outside variable :", a) #prints 5



# a=10  
# def local_global_vr(): # what if to have both global and local variable in a function
    
#     a=5  #local variable
#     x=globals()['a'] #global variable
#     print ("global variable:",x)#calling global variable prints 10
#     print("local variable:", a) #prints 5
#     print ("global variable using direct key:", globals()['a']) #prints 10
    

# local_global_vr()
# print("outside variable :", a) #prints 10




#nonlocal keywords
# def outside():
#     a=10
#     def inside():
#         a=100
#         print("inside a function:",a)

#     inside()
#     print("outside of inner funciton :",a)

# outside()    



# def outside():
#     a=10
#     def inside():
        
#         nonlocal a
#         a=100
#         print("inside a function:",a) #prints 100

#     inside()
#     print("outside of inner funciton :",a) #prints 100

# outside()    


# a=99
# def outside():
#     x=globals()['a']
#     a=10
#     def inside():
#         x=globals()['a']
#         nonlocal a
#         a=100
#         print("inside a function:",a,x) #prints 100, 99

#     inside()
#     print("outside of inner funciton :",a) #prints 100
#     print("outside of inner funciton :",x) #prints 99

# outside()
# print("outside of functions:",a)#prints 99



def outside():
    a=10
    def inside():
        j=int(input("type any no. :"))
        if j<=50:
            nonlocal a
            a=1000
            print("inside a function:",a) #prints 100

    inside()
    print("outside of inner funciton :",a) #prints 100

outside()    