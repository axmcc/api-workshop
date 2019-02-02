# WIM Python API workshop: 2019-02-01
# Helge Marahrens: hmarahre@iu.edu

# //- 1. read API documentation
# careful: this is a wrapper, not the API itself
# 1. they do not always make it easy to access the response
# 2. you have no guarantee that they respect the response limit

# //- 2. import packages
import wikipedia
import time
import pandas as pd
import csv
from collections import defaultdict

# //- 3. authentication
# no authentication needed

# //- 4. build get request
# //- 5. send get request – (check server response)
result = wikipedia.page("Tokyo")


# //- 6. explore data structures
print(result.url)
print(result.title)
print(result.coordinates)

# create a mini-dataframe of cities
city_list = ["Tokyo", "New York City", "Paris", "London", "Hannover, Germany"]
cities_dict = defaultdict(list)
for city in city_list:
    result = wikipedia.page(city)
    cities_dict[result.title] = [result.url,
                                 float(result.coordinates[0]),
                                 float(result.coordinates[1])]
df = pd.DataFrame.from_dict(cities_dict, orient='index')
df.columns = ['url', 'lat', 'long']

# //- 7. save data
## save as csv
#df.to_csv("cities.csv")
