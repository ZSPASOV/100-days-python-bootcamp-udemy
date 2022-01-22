import pandas

data = pandas.read_csv('./weather_data.csv')

# get data in a row
print(data[data.day == 'Friday'])