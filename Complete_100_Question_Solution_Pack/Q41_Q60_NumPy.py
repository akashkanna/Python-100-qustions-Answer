
import numpy as np

# Q41
arr=np.array([1,2,3,4])

# Q42
a=np.arange(1,21)

# Q43
z=np.zeros((3,3))

# Q44
o=np.ones((4,4))

# Q45
r=np.random.randint(1,101,10)

# Q46
print(a.shape,a.size)

# Q47
b=np.arange(12).reshape(3,4)

# Q48
print(b.flatten())

# Q49-Q52
x=np.array([1,2,3])
y=np.array([4,5,6])
print(x+y,x-y,x*y,x/y)

# Q53-Q60
print(np.min(x),np.max(y))
print(np.mean(x))
print(np.median(x))
print(np.std(x))
print(np.eye(5))
