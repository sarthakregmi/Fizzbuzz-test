#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(5,100):
    print("fizz"*(i%3<1) + (i%5<1)*"buzz" or i)
    print("Hello")


# In[ ]:




