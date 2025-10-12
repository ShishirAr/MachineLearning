print("hello this is my day of coding python!!!!")


seq=[2,3,4,5,6]
print(list(map(lambda x: x*3,seq)))


t= lambda x: x**2
print(t(12))


'''filter'''
print(list(filter(lambda num: num%2 ==0, seq)))


s='i am shishir!!'
b=s.split()
print(list(b))

d={'k1':1, 'k2':2}
d.items()


d=[12,3,3,444]
d.pop()
print(d)


x=[(1,2),(3,4),(5,6)]

for item in x:
    print(item)


print(7**4)

def domainGet(email):
    l=email.split("@")
    return l[1]


a=domainGet("shishir@gmail.com")
print(a)


def findDog(text):
    return "dog" in text

a=findDog("hello ")
print(a)


def dogCounter(text):
    count=0
    for word in text.split():
        if word=='dog':
            count=count+1
    return count

c=dogCounter("My dog is a  is very smart dog hotdog")


print(c)