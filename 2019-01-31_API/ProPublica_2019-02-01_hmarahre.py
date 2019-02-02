# WIM Python API workshop: 2019-02-01
# Helge Marahrens: hmarahre@iu.edu

# //- 1. read API documentation
# https://www.propublica.org/datastore/api/propublica-congress-api
# "Usage is limited to 5000 requests per day
# (rate limits are subject to change)."

# //- 2. import packages
import requests
import json
import time
import pandas as pd
import csv
import matplotlib.pyplot as plt

# //- 3. authentication
# set path to API key directory
#path = ""
#local_file = path + 'congress_auth.txt'
with open(local_file, "r") as txtfile:
    content = txtfile.readline().strip('\n')
# create dictionary with API key
credentials = {'X-API-Key':content}

# //- 4. build get request
# list of all members of the 114th house of representatives
host = "https://api.propublica.org/congress/v1/114"
chamber = "/house"
data_section = "/members.json"

# //- 5. send get request – check server response
response = requests.get(host + chamber + data_section, headers=credentials)
assert(response.status_code==200)
members = response.json()

# //- 6. explore data structures
print(len(members))
print(type(members))
print(members.keys())
print(len(members['results']))
print(members['results'][0].keys())
print(members['results'][0]['congress'])
#print([print(members['results'][0][key]) for key in ['congress', 'chamber', 'num_results', 'offset']])
print(type(members['results'][0]['members']))
print(len(members['results'][0]['members']))
print(json.dumps(members['results'][0]['members'][0], indent=4, sort_keys=True))

# //- 7. save data
# create a dataframe
df_114 = pd.DataFrame(members['results'][0]['members'])
df_114.shape
list(df_114)

# analyze data
plt.hist(pd.to_datetime(df_114['date_of_birth']))
plt.show()

# save as csv
#df_114.to_csv("congress_house_114.csv")
