import pandas

data = pandas.read_csv('./weather_data.csv')

temperature_list = data['temp'].to_list()
average_temp = sum(temperature_list) /  len(temperature_list)
print(average_temp)
# v2
print(data['temp'].mean())