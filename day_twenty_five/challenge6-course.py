import pandas

data = pandas.read_csv('./weather_data.csv')
# convert monday`s temperature to fahrenheit

monday = data[data.day == 'Monday']
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)