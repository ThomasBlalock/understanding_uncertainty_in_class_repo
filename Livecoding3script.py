# %%
import numpy as np
import pandas as pd
import requests
import json

# %%
cocktailurl = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail"
r = requests.get(cocktailurl)
r


# %%
r.text

# %%
myjson = json.loads(r.text)
#myjson = r.json()

# %%
myjson['drinks'][0]

# %%
myjson['drinks'][0]['strDrink']

# %%
#The modern way of converting to pandas df
cocktail_df = pd.json_normalize(myjson, record_path = ['drinks'])
cocktail_df

# %% [markdown]
# ## Wikipedia

# %%
wikiurl = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Virginia&format=json&srlimit=500"
r = requests.get(wikiurl)
r

# %%
r.text

# %% [markdown]
# ## User Agent

# %% [markdown]
# Getting a user-agent string
# The wrong ways - google what is my user-agent string, going to https://httpbin.org/user-agent

# %%
useragenturl = "https://httpbin.org/user-agent"

# %% [markdown]
# The Right way:

# %%
r = requests.get(useragenturl)
r

# %%
useragent = r.json()['user-agent']
useragent

# %%
headers = {'User-Agent': useragent, 'From':'atx6qu@virginia.edu'}
headers['User-Agent'] = 'ds6001/0.0 (atx6qu@virginia.edu) python-requests/2.32.5'

# %%
wikiurl = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Virginia&format=json&srlimit=500"
r = requests.get(wikiurl, headers=headers)
r

# %%
r.text

# %%
wiki_df = pd.json_normalize(r.json(), record_path = ['query','search'])
wiki_df

# %% [markdown]
# ## News API
# 
# DO NOT PASTE YOUR API KEY INTO YOUR CODE LIKE THIS!!

# %%
newskey ='d043c95b84114ef1bd85ae4e056399bd'

# %%
params = {'apikey':newskey, 'q':'Disc Golf'}

newsurl = 'https://newsapi.org/v2/everything'
r = requests.get(newsurl, headers=headers, params=params)
r

# %%
news_df = pd.json_normalize(r.json(), record_path=['articles'])
news_df


