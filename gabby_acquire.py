#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os

from env import host, user, password


# In[2]:


def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[14]:


sql_query = '''
            SELECT properties_2017.parcelid, properties_2017.id, bathroomcnt, bedroomcnt, calculatedbathnbr, calculatedfinishedsquarefeet, fips, latitude, longitude, regionidcounty, roomcnt, yearbuilt, taxvaluedollarcnt, taxamount, assessmentyear, propertycountylandusecode, propertylandusetypeid, transactiondate

            FROM properties_2017
            5JOIN predictions_2017 ON properties_2017.parcelid = predictions_2017.parcelid
            WHERE transactiondate BETWEEN '2017-05-01' AND '2017-06-30'
            AND propertylandusetypeid = '261' OR '262' OR '263' OR '264' OR '268' OR '273' OR '274' OR '275' OR '276' OR '279';
            
            '''
df = pd.read_sql(sql_query, get_connection('zillow'))
df.to_csv('zillow_df.csv')
df.info()


# In[15]:


def get_zillow_data():
    filename = "zillow_df.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('''SELECT properties_2017.parcelid, properties_2017.id, bathroomcnt, bedroomcnt, calculatedbathnbr, calculatedfinishedsquarefeet, fips, latitude, longitude, regionidcounty, roomcnt, yearbuilt, taxvaluedollarcnt, assessmentyear, propertycountylandusecode, propertylandusetypeid FROM properties_2017 JOIN predictions_2017 ON properties_2017.parcelid = predictions_2017.parcelid WHERE transactiondate BETWEEN '2017-05-01' AND '2017-06-30' AND propertylandusetypeid = '261' OR '262' OR '263' OR '264' OR '268' OR '273' OR '274' OR '275' OR '276' OR '279';''', get_connection('zillow'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)

        # Return the dataframe to the calling code
        return df  


# In[ ]:




