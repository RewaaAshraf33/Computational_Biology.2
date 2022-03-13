#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra


# In[4]:


from cobra import Model , Reaction , Metabolite


# In[9]:


model = Model ("first model")
### v0
v0=Reaction('v0')
v0.name='V0'
v0.lower_bound=1
v0.upper_bound=1
### v1
v1=Reaction('v1')
v1.name='V1'
v1.lower_bound=0
v1.upper_bound=1000
### v2
v2=Reaction('v2')
v2.name='V2'
v2.lower_bound=0
v2.upper_bound=1000
### M
M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000
### ATP
ATP_reaction=Reaction('ATP_reaction')
ATP_reaction.name='ATP_reaction'
ATP_reaction.lower_bound=0
ATP_reaction.upper_bound=1000
### v3
v3=Reaction('v3')
ATP_reaction.name='V3'
ATP_reaction.lower_bound=.9
ATP_reaction.upper_bound=.9


# In[10]:


A=Metabolite('A',compartment ='c')
B=Metabolite('B',compartment ='c')
C=Metabolite('C',compartment ='c')
ATP=Metabolite('ATP',compartment ='c')


# In[17]:


v1.add_metabolites({A:-1,B:1})
v2.add_metabolites({B:-1,C:1})
v0.add_metabolites({A:1})
M.add_metabolites({C:-1})
ATP_reaction.add_metabolites({A:-1,ATP:1})
v3.add_metabolites({ATP:-1})
model.add_reactions([v0,v1,ATP_reaction,v2,v3,M])


# In[20]:


model.objective='M'
model.optimize()


# In[21]:


model.summary()


# In[ ]:




