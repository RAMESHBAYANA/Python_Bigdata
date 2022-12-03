list1=[1,2,3,4,5,6]

new_list=[]     #Normal method
for i in list1:
    if i%2==0:
        new_list.append(i)
print(new_list)


result=[x for x in list1 if x%2==0]  # lsit comprehension method
print(result)


new_list=[]
for i in list1:
    new_list.append(i*5)
print(new_list)



new_list=[x*5 for x in list1]  #in list comprehension method
print(new_list)