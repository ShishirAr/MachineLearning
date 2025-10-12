print(2**3)

var=2 
print(var)

#strings

'single quotes'
"this is a string"

x='hello'
print(x)

num=12
name='sam'


'''order matters'''
print("my number is {} and my name is {}".format(num,name))   



'''order doesnt matters'''
print("my number is {one} and my name is {two}".format(one=num,two=name))


s='abcdefghijkl'
print(s[:4])
print(s[3:6])


my_list=[1,2,3,4,5,6]
my_list.append(8)
print(my_list)
print(my_list[0:3])
my_list[0]=100
print(my_list)


'''nested list'''
li=[1,2,3,[4,6,7,9,[3,6,7,['hi','world']]]]
print(li[3][4][3][1])



'''DICTINOARY'''
d={'key1':'value','key2':123}
print(d['key1'])
print(d['key2'])


d1={'k1':{'innerkey':[1,2,3]}}
a=d1['k1']['innerkey'][1]
print(a)

t=[6,7,8,89]
print(t[2])



'''sets'''
b={1,2,3,5,6,1,1,2}
print(b)
b.add(67)
print(b)

print(1<2 or 3>2)


if 1<2:

    print("HELL YEAH!!")

elif 4!=7:
    print("HUHHHHHHHHHHH!!")

elif 3==3:
    print("TRUEEEEEEEEEEEEE")

else:
    print("NOOOOOOOOOOO!!")




'''FOR LOOPS'''
seq=[2,3,4,5,6,7]
for num in seq:
    print(num)



'''while loop'''

i=1
while i<5:
    print('i is {}'.format(i))
    i=i+1



print(list(range(0,11)))

for x in range(0,5):
    print(x)


x=[1,2,3,4]
out = []

for num in x:
    out.append(num**2)

print(out)


'''list comprehension'''

newl=[n**2 for n in x]
print(newl)



'''functions'''

def my_func(name):
    print("Hello "+name)

print(my_func("shishir"))



def sqr(num):
    return num**2

'''this is docstring or comment
it can go multilLine
'''

out=sqr(4)
print(out)



def times2(var):
    return var*2

print(times2(5))


'''here I am using times2 func in a list which multiply each element of list by times 2, we are using map function which is pythons' built in function

it takes (function_name,targeted_list) as arguments
'''
seq=[1,2,3,4,5]
f=list(map(times2,seq))
print(f)


'''lambda expression'''
'''look at the above program and compare the difference'''
g=list(map(lambda n:n*3,seq))
print(g)





