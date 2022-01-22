import pandas

data = pandas.read_csv('./weather_data.csv')

data_dict = data.to_dict()

print(data['temp'])
temperature_list = data['temp'].to_list()
print(temperature_list)