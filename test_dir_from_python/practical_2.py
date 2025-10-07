myint = 4
type(myint)
print(myint)

myfloat = 0.1
type(myfloat)
print(myfloat)

mylist = ['a','b','c']
type(mylist)
print(mylist)

mystring = "goood morning America"
type(mystring)
print(mystring)

myboolean = 1 > 10
type(myboolean)
print(myboolean)

mydict = {"a": 0,"b":1}
type(mydict)
print(mydict)

myset = {1,2,2,3,4,5,4,6,"walter"}
type(myset)
print(myset)

myrange = range(10)
type(myrange)
print(myrange)

mytup = ('a','m','a')
type(mytup)
print(mytup)

if len(mystring) > 0:
    print("notempty")
else: 
    print("empty")


if myint > 0: 
    print("int is positive")
elif myint == 0:
    print("Int is zero")
elif mying < 0:
    print("Int is negative")


if type(mylist) is tuple or list or range:
     if len(mylist) == 0:
        print("empty")
     elif len(mylist) == 1:
        print ("single item")
     elif len(mylist) > 1:
        print("multiple items")
else: 
    print("wrong type for this task")
