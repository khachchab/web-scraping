#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup
import requests


# In[13]:


url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue#List_of_the_largest_companies'

page=requests.get(url)

soup= BeautifulSoup(page.text,'html')


# In[14]:


print(soup)


# In[15]:


soup.find('table')


# In[24]:


table=soup.find_all('table')[1]


# In[25]:


print(table)


# In[26]:


world_titles = table.find_all('th')


# In[27]:


world_titles


# In[28]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[29]:


import pandas as pd


# In[30]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[31]:


column_data = table.find_all('tr')


# In[33]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[34]:


df


# In[35]:


df.to_csv(r'C:\', index = False)


# In[ ]:




