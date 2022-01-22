import pandas

data = pandas.read_csv('./weather_data.csv')

check = data['temp'] == data['temp'].max()
print(type(check))
print(check)

another_check = data[data['temp'] == data['temp'].max()]
print(type(another_check))
print(another_check)