import pandas

data = pandas.read_csv('./weather_data.csv')

data_dict = data.to_dict()
print(data_dict)

print(data_dict['day'][4])