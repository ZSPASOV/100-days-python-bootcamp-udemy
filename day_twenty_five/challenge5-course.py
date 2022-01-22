# print the row of data which had the highest temperature

import pandas

data = pandas.read_csv('./weather_data.csv')

print(data[data.day == 'Monday'])