# def square_and_cube(n):
#     sqr=n*n
#     cube=n*n*n
#     return sqr,cube

# num=10
# s,c=square_and_cube(num)
# print(s,'and',c)
# print(square_and_cube(num))

# def sum(**kwargs):
#     print(kwargs['x'] + kwargs['y'])
#     print(kwargs)

# sum(x= 4,y= 6)



def connect(**kwargs):
    print(kwargs)
    print(kwargs.items())
    print(kwargs.keys())
    print(kwargs.values())
    print("key name=",kwargs['host'], ", keyname=",kwargs['landmark'])
    for k,v in kwargs.items():
        print('keys',k,'values',v)
connect(host = 'iaf', port= 12345, pwd= 'qwerty', landmark='bangalore')  #function



# connect={'host':'iaf','port': 12345, 'pwd' : 'qwerty', 'landmark':'bangalore'} #dictionary
# connect['host']='civilian'
# print (connect)
# print(connect['host'])


# # a,b = 1,2
# # print(a)


# def sum_of_num(listx):
#     sum=0
#     for x in listx:
#         sum=sum+x
#         print(x)
#     print(sum)

# list1=[1,2,3,4,5]
# sum_of_num(list1)