#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1,101):
    print("fizz"*(i%3<1) + (i%5<1)*"buzz" or i)
    


# In[ ]:




