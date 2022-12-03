
e={'name': 'ramesh', 'age': 35}
# print(d)

d={}
d['name']= 'ramesh'
d['age']=35
d['service']= ['air force', 'it']
# f={'ra':'ma'}
# print(f['ra'])
# f['attached']= d
# print(d['service'][1])
# print(f['attached']['service'][1])
# # d['age']= 40
# d['service'][1]='cwa'
# # print(d['service'])
# print(d)
# only_keys=d.keys()
# print(only_keys) #to know the keys
# print(list(d.keys()))
# print(list(only_keys))# to convert in list form
# print(list(d.values()))
# print(d.items())


# for k in  d.keys():
#     print('key name is',k,)

# for k,v in d.items():
#     print('key name is',k,'value name is',v)

# print(d.get('age'))
# print(d['age'])



# d={}
# d['name']= 'ramesh'
# d['age']=35
# d['service']= ['air force', 'it']
# onlykeys=list(d.keys()) # to check the keys name in the given dictionary
# print(onlykeys)
# for check in range(0,len(onlykeys)):
#     if onlykeys[check] == 'rank':
#         print('true')
#         break
# else:
#     print('false')    


connect={'host':'iaf','port': 12345, 'pwd' : 'qwerty', 'landmark':'bangalore'} 
connect['host']='civilian'
print (connect)
print(connect['host'])
