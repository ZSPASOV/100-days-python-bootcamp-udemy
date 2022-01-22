import pandas

data = pandas.read_csv('./weather_data.csv')
print(type(data))
print(type(data['temp']))