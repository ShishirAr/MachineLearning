my_list=[3,4,5]
import numpy as np

arr= np.array(my_list)

print(arr)

arr_2d=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(arr_2d))


d=np.arange(0,12,3)   
'''create range of array'''
print(d)



'''3 rows and 2 columns'''
print(np.zeros((3,2))) 



print(np.ones((2,3)))


print(np.linspace(0,5,10))


print(np.eye(4))    
'''identity matrixx'''


print(np.random.rand(4))


g=(np.random.randint(1,100,10))
'''10 random array from 1 inclusive to 100 exclusive '''



print(g.reshape(5,2))

print(g.max())
print(g.min())


print(g.argmax())
print(g.argmin())

print(g.shape)
