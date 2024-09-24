#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing numpy
import numpy as np
print(np.__version__)

#creating array
# In[3]:


# creating arrays 0-d, 1-d, 2-d,3-d
# 0-d
a=np.array(10)
a


# In[6]:


# 1-d
a=np.array([10,20,30])
print(a)


# In[7]:


a=np.array([10,20,30,40])
a


# In[9]:


# 2-d
a=np.array([[1,2,3,4],[1,2,3,4]])
print(a)
print(a[1][1])


# In[10]:


# 3-d
a=np.array([[[10,20],[30,40]]
           ,[[50,60],[70,80]]])
print(a)
print(a[1][1][1])


# In[14]:


#asarray() function
a=[10,20,30,40]
b=np.asarray(a, dtype=float)
print(b)
print("using nditer() function")
for i in np.nditer(b):
    print(i)


# In[21]:


# handling string
# using frombuffer()
a=b"hi i am siva from andhra university"
print(np.frombuffer(a, dtype='S1'))
np.frombuffer(a, dtype='S1',count=10)


# In[25]:


# fromiter() function
a=[10,20,30,40,50]
print(np.fromiter(a, dtype=int))
np.fromiter(a, dtype=float, count=3)


# In[ ]:


#initializing array


# In[26]:


# zeros() function
a=np.zeros(3)
b=np.zeros([2,3],dtype=float)
print(a)
print(b)


# In[28]:


# full() function
a=np.full([2,3],1)
b=np.full([3,5], 10)
c=np.full([3,3],5)
print(a)
print(b)
print(c)


# In[30]:


# random.rand() function
a=np.random.rand(2,3)
print(a)


# In[31]:


# ones() function
a=np.ones([2,3])
print(a)


# In[32]:


# eye() function
a=np.eye(5)
print(a)


# In[39]:


# arang() function start stop step and also reshape() function
a=np.arange(1,10,1)
b=np.arange(0,100,10)
c=np.arange(0,50,5, dtype=float)
print(a)
print(b)
print(c)
print(b.reshape(2,5))


# # array operations

# In[41]:


# accessing and slicing operations
a=np.array([[1,2,3,4,5],[10,20,30,40,50]])
print(a[0][4])
b=np.arange(0,100,10)
print(b[2:4])


# In[43]:


# copy() function
a=np.arange(0,10)
b=np.copy(a)
print(a)
print(b)


# In[44]:


#reshape() function
c=a.reshape(2,5)
print(c)


# In[45]:


#append() function
d=np.append(a,b)
print(d)


# In[46]:


# insert() function
e=np.insert(d,10,45)
print(e)


# In[48]:


# delete() function
f=np.delete(e,10)
print(f)


# In[51]:


# concatenate() function
a=np.array([10,20,30])
b=np.array([40,50,60])
g=np.concatenate(a,b)
print(g)


# In[53]:


# sort() function
a=np.random.rand(10)
print(np.sort(a))


# In[57]:


# search sorted
a=([1,49,39,64,83,7,9])
print(np.searchsorted(a,64))
print(np.searchsorted(a,[49,64]))


# In[62]:


# where() function
a=np.arange(0,140,10)
print(a)
np.where(a==3)


# # arithametic operations

# In[64]:


a=np.array([10,20,30,40])
b=np.array([1,2,3,4])

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.exp(a))
print(np.sqrt(a))


# In[66]:


# comparision() function
print(np.array_equal(a,b))  # array wise comparision
a==b                        # element wise comparition


# # array functions

# In[71]:


a= np.array([10,20,30,40,50,60,70,80,90,100])
print(np.min(a,axis=0))
print(np.max(a, axis=0))
print(np.sum(a, axis=0))
print(np.mean(a, axis=0))
print(np.median(a, axis=0))
print(np.var(a, axis=0))
print(np.std(a, axis=0))


# In[ ]:




