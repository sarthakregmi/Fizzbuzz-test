#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(2,200):
    print("fizz"*(i%3<1) + (i%5<1)*"buzz" or i)
    print("Hello")
    print("World")


# In[ ]:




