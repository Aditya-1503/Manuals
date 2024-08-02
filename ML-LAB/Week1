#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
X = np.reshape(X, (-1,3))


# In[3]:


print(X)
#[[0 1 2]
# [3 4 5]
# [6 7 8]]

# In[4]:


X[X % 2 == 1] = -1


# In[5]:


print(X)
#[[ 0 -1  2]
# [-1  4 -1]
# [ 6 -1  8]]

# In[6]:


x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])


# In[7]:


mask_greater = (x > y)
mask_equal = (x == y)
positions_greater = np.where(mask_greater)[0]
positions_equal = np.where(mask_equal)[0]


# In[8]:


print(positions_greater, positions_equal)
# [1 2 4 5 6 7 8 9] [0]



# In[10]:


newX = np.arange(100).reshape(5, -1)


# In[11]:


print(newX[:,:4])
#[[ 0  1  2  3]
# [20 21 22 23]
# [40 41 42 43]
# [60 61 62 63]
# [80 81 82 83]]


# In[12]:


randArr = np.random.randint(30,41, [10])


# In[13]:


print(randArr)
# [39 37 38 40 36 32 34 32 32 31]


# In[14]:


A = np.array(([1,2,3], [4,5,6], [7,8,10]))
B = np.array(([7,8,10], [4,5,6], [1,2,3]))


# In[15]:


C = np.add(A, B)


# In[16]:


E = np.subtract(A,B)


# In[17]:


print(np.sum(A)) #sum of all elements in A
print(np.sum(B, axis = 0)) # sum of all columns in B
print(np.sum(C, axis = 1))
#46
#[12 15 19]
#[31 30 31]

# In[18]:


D = np.dot(A,B)


# In[19]:


print(D)
#[[ 18  24  31]
# [ 54  69  88]
# [ 91 116 148]]

# In[20]:


E = np.sort(C)


# In[21]:


print(E)
#[[ 8 10 13]
# [ 8 10 12]
# [ 8 10 13]]

# In[22]:


print(np.transpose(E))
#[[ 8  8  8]
# [10 10 10]
# [13 12 13]]




