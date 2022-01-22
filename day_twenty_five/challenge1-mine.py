with open('./weather_data.csv') as weather_data:
    data = [row.strip() for row in weather_data.readlines()]
    print(data)