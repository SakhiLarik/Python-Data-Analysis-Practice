#!/usr/bin/env python
# coding: utf-8

# # Numpy
# #### Numpy Is The Core Library For Scientific Computation In Python
# #### It Provides a high-performance multidimentional array objects, and tools for working with these arrays
# ### It covers less memory then the list and it is faster then list and it is convenient

# In[27]:


import numpy as np
import matplotlib.pyplot as plt
import time
import sys
a = np.array({(1,2,3),(4,5,6),(7,8,9)})
b = np.array([(1,2,3),(4,5,6),(7,8,9)])
c = np.array(((1,2,3),(4,5,6),(7,8,9)))
print(a)
print(b,"\n")
print(c)
print("\nLet's Look At Memory Allocation")
S = range(1000)
print(sys.getsizeof(0)*len(S),"Size Allocated By The List") # Size Allocated By The List
D = np.arange(1000)
print(D.size*D.itemsize,"Size Allocated By The Numpy\n") # Size Allocated By The Numpy
print("Let's Look At Time Duration Allocation")
SIZE = 1000000
L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2= np.arange(SIZE)
start = time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000,"Time Covered By List\n")
start = time.time()
result = A1+A2
print((time.time()-start)*1000,"Time Covered By numpy\n")
print("Finding The Dimension Of An Array \n")
dime = np.array([(1,2,3),(4,5,6)])
print(dime.ndim) # Dimesion Of An Array
print("Finding The Byte Size Of An Array \n")
btsize = np.array([(1,2,3),(4,5,6)])
print(btsize.itemsize)# Item Byte Size Of An Array
print(btsize.dtype)# Data Type Of An Array
print(btsize.size)# Size Of An Array
print(btsize.shape)# Shape Of An Array
print(" Converting The Shape Of An Anrray \n")
convert = np.array([(1,2,3,4,5),(6,7,8,9,0)])
print(convert,"\n")
print(convert.shape,"\n")
con = convert.reshape(5,2)
print(con,"\n")
print(con.shape,"\n")
print("Slicing An Anrray \n")
Slice = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(Slice[0,2])
print(Slice[0:,2])
print(Slice[0:2,2])
print(" Line Spacing An Anrray \n")
LinSpace = np.linspace(1,50,10)
print(LinSpace)
print(" Other Operation Of An Anrray \n")
minmax = np.array([(1,2,3),(4,5,6)])
print("Minium ",minmax.min())
print("\nMaxium ",minmax.max())
print("\nSum Of Array ",minmax.sum())
print("\nSum Of Rows = ",minmax.sum(axis=0))
print("\nSum Of Columns = ",minmax.sum(axis=1))
print("\nLet's Look At The Numpy Square Root and Standared Davietation Of Numpy Array")
newarray = np.array([1,4,9])
print("\nSquare root of array is = ",np.sqrt(newarray))
print("\ndaviation of array is = ",np.std(newarray))
print("\nLet's Look At The Numpy Arthamatic Operation")
array1 = np.array([(1,2,3),(4,5,6)])
array2 = np.array([(1,2,3),(4,5,6)])
addition = array1+array2
subtraction = array1-array2
division = array1/array2
multiplication = array1*array2
modulas = array1%array2
print("\nAddition Of Array is = ",addition)
print("\nsubtraction Of Array is = ",subtraction)
print("\ndivision Of Array is = ",division)
print("\nmultiplication Of Array is = ",multiplication)
print("\nmodulas Of Array is = ",modulas)
print("\nLet's Look At The Numpy vartical stack and horizental stack Of Numpy Array")
i = np.array([(1,2,3),(4,5,6)])
j = np.array([(1,2,3),(4,5,6)])
print("\nVartical Stack = ",np.vstack(i))
print("\nHorizental Stack = ",np.hstack(i))
print("ravel = ",np.ravel(i))
print("\nLet's Look At The Numpy special function Of Numpy Array")
print("\nSine Function And Cosine Function")
x = np.arange(0,8,0.3)
y = np.sin(x)
z = np.cos(x)
w = np.tan(x)
#print("Sine Plot = ",plt.plot(x,y))
#print("cosine Plot = ",plt.plot(x,z))
print("tan Plot = ",plt.plot(x,w))
plt.show()


# In[ ]:




