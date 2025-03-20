#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from os.path import isdir
import os
import geokit as gk
import matplotlib.pyplot as plt


# In[2]:


syn_el_shape = np.array([0.021008403, 0.021008403, 0.021008403, 0.021008403, 0.027310924, 0.037815126,
                         0.042016807, 0.042016807, 0.042016807, 0.042016807, 0.042016807, 0.042016807,
                         0.042016807, 0.042016807, 0.042016807, 0.042016807, 0.046218487, 0.050420168,
                         0.067226891, 0.084033613, 0.073529412, 0.052521008, 0.033613445, 0.023109244])

syn_h2_shape = np.array([0.1847, 0.1063, 0.0732, 0.0871, 0.1272, 0.2631, 0.4878, 0.8624, 
                         1.2439, 1.2125, 1.1063, 1.0958, 1.1341, 1.1585, 1.1289, 1.2160, 
                         1.4477, 1.7579, 1.6916, 1.3241, 0.8955, 0.5366, 0.3833, 0.2683])

syn_h2_shape = (syn_h2_shape / syn_h2_shape.sum())

def create_synthetic_load(daily_load_shape):

    syn_load_curve_y = np.tile(daily_load_shape, 365)
    syn_load_curve_y = pd.DataFrame(syn_load_curve_y) / 365
    
    return syn_load_curve_y


# In[3]:


fig, ax = plt.subplots(figsize=(12,5))
ax.plot(create_synthetic_load(syn_h2_shape)[0:24*7], '--',  label="Load")


# In[27]:


GID_0 = "NER"
regions = gk.vector.extractFeatures(f"data/regions/region_shape_{GID_0}.shp", onlyAttr=True)


# In[5]:


num_regions = len(regions.region_id)
syn_el_load_per_region = pd.concat([create_synthetic_load(syn_el_shape)] * (num_regions), axis=1, ignore_index=True)
syn_h2_load_per_region = pd.concat([create_synthetic_load(syn_h2_shape)] * (num_regions), axis=1, ignore_index=True)


# In[6]:


syn_el_load_per_region.columns = regions.region_id.to_list()
syn_h2_load_per_region.columns = regions.region_id.to_list()


# In[9]:


syn_h2_load_per_region


# In[10]:


pop = pd.read_excel(r"data/miscellaneous/NER_pop_per_region.xlsx", engine="openpyxl", index_col=0)
gdp = pd.read_excel(r"data/miscellaneous/NER_gdp_per_region.xlsx", engine="openpyxl", index_col=0)


# In[11]:


national_el_dem = 2000 # GWh
national_h2_dem = 2 * 33.33 # Mt --> GWh


# In[12]:


pop["el_dem"] = pop["pop_fraction"]*national_el_dem
gdp["h2_dem"] = gdp["gdp_fraction"]*national_h2_dem


# In[13]:


pop.set_index("GID_1")["el_dem"]


# In[19]:


syn_el_load_per_region = pop.set_index("GID_1")["el_dem"] * syn_el_load_per_region


# In[21]:


syn_h2_load_per_region = gdp.set_index("GID_1")["h2_dem"] * syn_h2_load_per_region


# In[25]:


if not isdir("data/sinks/"):
    os.makedirs("data/sinks/")


# In[28]:


syn_el_load_per_region.to_excel(f"data/sinks/electricity_dem_{GID_0}.xlsx")
syn_h2_load_per_region.to_excel(f"data/sinks/hydrogen_dem_{GID_0}.xlsx")


# In[1]:

# In[ ]:




