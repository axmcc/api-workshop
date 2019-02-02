# WIM Python API workshop: 2019-02-01
# Helge Marahrens: hmarahre@iu.edu

# //- 1. read API documentation
# Description: "The Data USA API allows users to access slices of data
# across multiple government sources. Data is available in both JSON
# and CSV formats."
# https://github.com/DataUSA/datausa-api/wiki/DataAPI

# //- 2. import packages
import requests
import json
import time
import pandas as pd
import csv
import matplotlib.pyplot as plt

# //- 3. authentication
# no authentication needed

# //- 4. build get request
host = 'http://api.datausa.io/api/'
params = "?show=cip&sumlevel=2"
year = "&year=latest"
columns = "&required=grads_total,grads_men,grads_women"
url = host + params + year + columns
print(url)

# //- 5. send get request – check server response
response = requests.get(url)
assert(response.status_code==200)
print(response)
data = response.json()

# //- 6. explore data structures
type(data)
data.keys()
json.dumps(data, sort_keys=True, indent=4)
data['headers']
data['data'][0]

df = pd.DataFrame.from_dict([d for d in data["data"]])
df.columns = data['headers']
# CIP codes: https://nces.ed.gov/ipeds/cipcode/browse.aspx?y=55
df.sort_values('grads_total', ascending=False)

# percent men
df['perc_men'] = (df['grads_men']/df['grads_total'])*100
df['perc_men'].describe()

# histogram percent men
plt.hist(df['perc_men'])
plt.show()

# change since 2014?
year = "&year=2014"
#year = "&year=oldest"
url = host + params + year + columns
print(url)
time.sleep(5)
response_2014 = requests.request('GET', url)
assert(response.status_code==200)
data_2014 = response_2014.json()
df_2014 = pd.DataFrame.from_dict([d for d in data_2014["data"]])
df_2014.columns = data_2014['headers']
df_2014['perc_men'] = (df_2014['grads_men']/df_2014['grads_total'])*100
df_change = df.append(df_2014).reset_index()

# percent men by year
plt.hist(df_change.loc[df_change['year']==2016,'perc_men'], alpha=.5)
plt.hist(df_change.loc[df_change['year']==2014,'perc_men'], alpha=.5,\
         color='red')
plt.show()

# //- 7. save data
## save as csv
#df_change.to_csv("IPEDS_change.csv")
