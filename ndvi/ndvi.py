#!/usr/bin/env python
# coding: utf-8

# # NDVI calculation with xcube-stac

# In[1]:


import xarray as xr
from xcube.core.store import new_data_store


# Set credentials, if needed.

# In[2]:


credentials = {
    "key": "insert S3 key here",
    "secret": "insert S3 secret here",
}


# Instantiate a CDSE STAC store. This will require valid CDSE S3 credentials.

# In[3]:


store = new_data_store("stac-cdse", stack_mode=False, **credentials)


# Alternative syntax for non-CDSE stores, specifying STAC root URL explicitly.

# In[4]:


# store = new_data_store("stac", stack_mode=False, url="https://earth-search.aws.element84.com/v1")


# Select a product on which to perform the calculation.

# In[5]:


product_id = "S2A_MSIL2A_20250321T102731_N0511_R108_T32UNE_20250321T122920"


# Open the dataset and show a summary of its metadata.

# In[6]:


ds = store.open_data(
    data_id=f"collections/sentinel-2-l2a/items/{product_id}"
)
ds


# Calculate the NDVI, store it in a new dataset, and show a summary of the new dataset’s metadata.

# In[7]:


ndvi = xr.Dataset(data_vars={"ndvi": (ds.B08 - ds.B04) / (ds.B08 + ds.B04)})
ndvi


# Write the data to a local Zarr archive.

# In[8]:


ndvi.to_zarr("ndvi.zarr")

