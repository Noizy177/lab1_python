#!/usr/bin/env python
# coding: utf-8

# In[15]:


def frange(start, finish, step):
    x = start
    if step > 0:
        while x < finish:
            yield round(x,2)
            x = x + step
    else:
        while x > finish:
            yield round(x,2)
            x = x + step

for x in frange(1,5,0.1):
    print(x)


# In[ ]:




