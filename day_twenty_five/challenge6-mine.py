import pandas

data = pandas.read_csv('./weather_data.csv')
# convert monday`s temperature to fahrenheit
monday_temp = data[data['day'] == 'Monday']['temp']
print(monday_temp)

print(monday_temp.to_list()[0] * 9 / 5 + 32)



