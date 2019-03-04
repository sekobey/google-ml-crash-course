import pandas as pd

print(pd.__version__)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({'City Name': city_names, 'Population': population})

print(type(cities['City Name']))

print(cities['City Name'])

print(type(cities['City Name'][1]))

print(cities['City Name'][1])

print(type(cities[0:2]))

print(cities[0:2])

population = cities['Population'
]
print(population / 1000)

import numpy as np

print(np.log(population))

population.apply(lambda val: val > 1000000)

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
#cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)

cities['Is wide and saint'] = (cities['Area square miles'] > 50) & cities['City Name'].apply(lambda name: name.startswith('San '))

print(cities)

#california_housing_dataframe = pd.read_csv(
#    "https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

# print(california_housing_dataframe.describe())

# print(california_housing_dataframe.head())

# california_housing_dataframe.hist('housing_median_age')

