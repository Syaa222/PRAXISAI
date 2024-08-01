'''
Tupple
'''

# assign list
mylist = ['Seblak, cipak koceak, mie jebew']
mylist2 = [1,2,3,4] 
mylist3 = [1, 2.0, 'laper']

# print a list
print (mylist3)

# print specific member of a list
print (mylist[2])

#change specific list member
mylist[1] = 'Laper banget'
print(mylist)

# sort a list 
mylist.sort()
#print (mylist)

'''
Tupple
'''

#assign a tuple
mytuple = ('seblak', 'cipak koceak', 'mie jebew')
print(mytuple)

# try to change tuple
# mytuple[0] = 'Laper'

#asign a set
myset = {'seblak', 'cipak koceak', 'mie jebew'}

for x in myset:
    print(x)

'''
DICTIONARY
'''
# assign a dictionary
# dictionary = {idkey:Value}
mydict = { "brand": "Ford", "model": "Mustang","year": 1964}
print(mydict["model"])