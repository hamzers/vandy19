#!/usr/bin/env python
# coding: utf-8

# In[99]:


import requests
import pprint


# In[100]:


payload = {'api_key': '2kouWHaiA0UlxQpKyi9GcsC7uQz1irGv', 'q': 'cheeseburgers', 'limit': 1, 'lang': 'en'}
r = requests.get('http://api.giphy.com/v1/gifs/search', params=payload)
print(r.url)


# In[103]:


def gotData(stuff):
    print(stuff.json())


# In[111]:


pprint.pprint(r.json()['data'][0]['images']['original']['url'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




