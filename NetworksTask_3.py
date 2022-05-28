#!/usr/bin/env python
# coding: utf-8

# In[4]:


import networkx as nx


# In[5]:


G = nx.Graph()
G.add_nodes_from(['a', 'b', 'c', 'd'])
G.add_edges_from([('a','b'), ('b','c'), ('c','d'), ('a','c')])
nx.draw(G, with_labels = True)


# In[5]:


list(G.neighbors('b'))


# In[6]:


for neighbor in G.neighbors('b'):
    print(neighbor)


# In[7]:


G.has_node('a')


# In[8]:


nx.is_tree(G)


# In[9]:


nx.is_connected(G)


# In[10]:


G.degree('a')


# In[11]:


D = nx.DiGraph()
D.add_edges_from([('1','2'), ('2','3'), ('1','4'), ('3','4')])
nx.draw(D, with_labels = True)


# In[12]:


X=nx.Graph()
X.add_edges_from([(1,2),(2,3),(1,3),(3,4)])
nx.draw(X,with_labels=True,node_size=500)


# In[13]:


dict(X.degree())


# In[15]:


nx.to_numpy_matrix(X)


# In[3]:


graph=nx.read_edgelist('graph.txt',nodetype=str,create_using=nx.DiGraph())
nx.draw(graph,with_labels=True,node_size=500)


# In[ ]:




