import pandas

data = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


# count the squirels

squirel_color = data['Primary Fur Color']
print(squirel_color.value_counts(dropna=False))

