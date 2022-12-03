


# for n in range(1,11):
#     print(n)


# s=int(input("enter start range of no.s :"))
# e=int(input("enter end range of no.s :"))
# for num in range(s, e):
#     print(num)



# for num in (1,6,5,7):
    # print(num)



# s=int(input("enter start range of no.s :"))
# e=int(input("enter end range of no.s :"))
# n=int(input("enter time of increment range :"))
# for num in range (s,e,n):
#      print(num)



# start=int(input("enter start range of no.s :"))
# end=int(input("enter end range of no.s :"))
# times=int(input("enter time of increment range :"))
# if start > end:
#     for num in range (start,end,-times):
#         print(num)   
# else:
#     print ('start no. should be less than end range no.')     


# num_list = [2,5,8,-5,6]
# sum = 0
# for num in num_list:
#     sum = sum + num
# print (sum)


# print("give any 5 no.s")
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# num_list = [a,b,c,d,e]
# sum = 0
# for num in num_list:
#     sum = sum + num
# print ("the sum of above given no. is :", sum)



# sum=0
# for x in (1,5,16,3,6,9,11,23,54):
#     if x<10:
#         sum = sum + x
#         print(x)
# print (sum)
       


       
# a=int(input())
# b=int(input())
# sum=0
# if a < b:
#     print("the range is")
#     for num in range (a,b):
#         #if a>b:
#             sum=sum+num
#             print(num)
#     print("the sum is:",sum)   
# else:
#     print ('start no. should be greater than end range no.')     


# sum=0
# table = int(input("please enter the table No. ")) #tables
# for num in range (1,11):
#     sum=sum+num
#     x=table*num



# table = int(input("please enter the table No. "))
# upto=int(input("please enter the table No. upto : ")) #tables using while loop
# counter=0
# while counter <= upto:
#     ans= table * counter
#     print(table, " x " , counter ," = ",  ans)
#     counter= counter + 1


# l1=[]
# l1.append(3)
# l1.append(4)
# l1.append(5)
# print(l1)



# List_num = []
# for num in range(1,11):
#     List_num.append(num)
# print(List_num)
    

# for numeric in range(1,10,-(-1)):
#     print(numeric)


list1=[1,2,3,4,5,6]
new_list=[]
for i in list1:
    new_list.append(i*10)
print(new_list)    


for i in list1:
    new=i*10
    print(new)    



# def test(a):
#     # l=[]
#     if type(a)== int:
#         for i in range(0,a):
#             # print("*", end= " H")
#             for j in range (0,i+1):
#                 print(".",end= " ")
#             print("\r")
#             # l.append(".")
#             # print (l)

# test(3)

# # def test1(a):
# #     if type(a)==int:
#         for i in range(0,a):
#             for j in range(0,i+1):
#                 print(".",end=" ")
#             print("\r")

# test1(3)  

# def test2(n):
#     if type(n)==int:
#         for i in range (0,5):
#             for j in range(0,i+1):
#                 print("#", end=" ")
#             print()

# test2(5)   

def test3(r):
    c=r-1
    for i in range(0,r):
        for j in range(0,c):
            print(end=" ")
        c=c-1
        for j in range(0,i+1):
            print("*",end=" ")

        print("\n") 

test3(5)            



Hi copied from github