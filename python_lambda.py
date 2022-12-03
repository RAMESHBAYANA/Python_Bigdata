# num = lambda x:x+1
# n=10
# print(num(n))

# num = lambda x,y : x+y
# m=40
# n=10  # or we can give m,n = 10,40
# print(num(m,n))


# num = lambda str1,str2 : str1+str2
# print(num('ram','esh'))


# num = lambda x,y : x if x>y else y
# num1,num2=7,3
# print(num(num1,num2))


# highest_num= lambda x,y,z : x if x>y and x>z else ( y if y>z else z)
# f=int(input("enter first num  :"))
# s=int(input("enter second num  :"))
# t=int(input("enter third num  :"))

# # f,s,t=1,2,4
# Ans_is = highest_num(f,s,t)
# print("the highest of given nums is",Ans_is) 
# print("the highest of given nums is",highest_num(f,s,t)) 


# mapping

list_of_num = [1,2,3,4,5,6]
square_of_list = lambda x: x*x
ans_is=list(map(square_of_list,list_of_num))
print(ans_is)


# list1 = [1,2,3,4,5,6,7,8,9]
# square_num = lambda x : x*x
# square_list = list(map(square_num, list1))
# print(square_list)


# list1=[2,4,6,8]
# list2=[1,3,5,7]
# sum_of_lists= lambda x,y : x+y
# Ans_is = list(map(sum_of_lists,list1,list2))
# print(Ans_is)


# How to use reduce ??
# import functools

# list_x = [1,2,3,4,5]
# add_all_nums = lambda x , y : x + y

# result = functools.reduce(add_all_nums ,list_x)
# print(result)

# multiply_all_nums  = lambda x , y : x * y
# result = functools.reduce(multiply_all_nums , list_x)
# print(result)


# list1=[10,20,30]
# def sum(x):
#     z=0
#     for add in x:
#         z=z+add
#     print(z)
# sum(list1)




# def sum_of_num(listx):
#     sum=0
#     for x in listx:
#         if x<= 5:
#             sum=sum+x
#             print(x)
#     print(sum)

# list1=[1,2,3,4,5,6,7,8,9,10]
# sum_of_num(list1)


mul=lambda x:x*10
list2=[1,2,3,4]
print(list((map(mul,list2))))


def mul(x):
    k=1
    for j in x:
        k=j*10
        print(k)

listc=[1,2,3,4]
mul(listc)

# using reduce
# import functools

# sum=lambda x,y : x+y
# list1=[1,2,3,4,5]
# print(functools.reduce(sum,list1))

# How to use filter ()

# Create list of only odd elements
# seq = [1,2,5,6,9,7,10]

# filter_odd = lambda x : x % 2 != 0

# result = list(filter(filter_odd , seq))
# print(result)

# filter_even = lambda x : x % 2 == 0

# result = list(filter(filter_even , seq))
# print(result)