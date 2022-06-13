#!/usr/bin/env python
# coding: utf-8

# In[17]:


from elasticsearch import Elasticsearch, helpers
import configparser


# In[18]:


config = configparser.ConfigParser()


# In[19]:


config.read('example.ini')


# In[20]:


es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    http_auth=(config['ELASTIC']['user'], config['ELASTIC']['password'])
)


# In[21]:


es.info()


# In[28]:


es.index(
 index='lord-of-the-rings',
 document={
  'character': 'Aragon',
  'quote': 'It is not this day.'
 })


# In[ ]:
es.index(
 index='lord-of-the-rings',
 document={
  'character': 'Gandalf',
  'quote': 'A wizard is never late, nor is he early.'
 })

es.indices.refresh(index='lord-of-the-rings')

result = es.search(
 index='lord-of-the-rings',
  query={
    'match': {'quote': 'late'}
  }
 )

result['hits']['hits']


# %%
