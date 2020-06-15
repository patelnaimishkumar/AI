import numpy as np
a1=np.array([1,2,3,4])
print(a1)
print(type(a1))
a2=np.array([[[[1,2,3],[4,5,6]]]])
print(a2)
print(a2.dtype)
print(a2.ndim)
print(a2.shape)
#r=range(5.)
r=np.arange(5.)
print(r)
rand=np.random.rand(4,5)
print(rand)
#rand=np.linspace(4,5,1000)
#print(rand)
rand=np.zeros((4,5,3))
print(rand)
print(rand.ndim)
print(rand.shape)
rand=np.ones((4,5,3))
print(rand)
print(rand.ndim)
print(rand.shape)

rand=np.eye((3))
print(rand)
print(rand.ndim)
print(rand.shape)




rand=np.random.randint(4,10,(3,4))
print(rand)
print(rand.ndim)
print(rand.shape)




