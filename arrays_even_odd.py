
# coding: utf-8

# In[7]:


# we want to bring the even elements to the front of the array
# done my partitioning the array and not allocating any extra memory

def bring_even_front(A):
    next_even, next_odd = 0, len(A)-1
    while next_even <= next_odd:
        if A[next_even]%2 == 0:
            next_even+=1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd-=1


# In[13]:


rays = [5, 3, 5, 1, 6, 3, 6]


# In[14]:


print(rays)


# In[15]:


bring_even_front(rays)


# In[16]:


print(rays)

