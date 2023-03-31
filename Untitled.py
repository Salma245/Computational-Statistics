#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
a=np.array([1,2,3,4,5])
print(type(a))
print(a.ndim)
print(np.shape(a))


# In[11]:


a1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
a=np.asarray(a1,float,'F')
print(a)
for i in np.nditer(a):
  print(i)


# In[21]:


a1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
a=np.asarray(a1,float,'F')
print(a)
for i in np.nditer(a):
    print(i)


# In[28]:


n=np.arange(0,10,2)
print(n)
n1=np.linspace(0,20,5)
print(n1)


# In[33]:


z=np.zeros((3,3))
print(z)


# In[37]:


z=np.ones((3,3))
print(z)


# In[71]:


import math
a=[[6,7,8,4,5],[1,8,3,9,2]]
print(a)
l=0
s=0    
for i in a:
    for j in i:
        s=s+j
        l=l+1
mean=s/l
print(mean)
v=0
for i in a:
    for j in i:
        v+=(j-mean)*(j-mean)
variance=v/l
print(variance)
std=math.sqrt(variance)
print(std)
print(np.std(a))


# In[72]:


a=[[6,7,8,4,5],[1,8,3,9,2]]
l=len(a[0])
print(l)
e=len(a)
print(e)
d=(l)//2
s=0
print(d)
if(l%2==0):
    for i in range(len(a)):
        s+=(a[i][d]+a[i][d-1])//2
else:
    for i in range(len(a)):
        s+=a[i][d]
median=s/e
print(median)
print(np.median(a))
        
        
            


# In[ ]:




