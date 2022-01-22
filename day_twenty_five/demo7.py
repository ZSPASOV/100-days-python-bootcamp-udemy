import pandas

data = pandas.read_csv('./weather_data.csv')

# v1
print(data['condition'])

# v2
print(data.condition)