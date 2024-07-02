import pandas

# with open("C:\Python\Python 100 Days\Day 25\weather_data.csv") as data_files:
    
#     data = data_files.readlines()
    
#     print(data)

# import csv

# with open ("C:\Python\Python 100 Days\Day 25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
            
#     print(temperature)


# data = pandas.read_csv("C:\Python\Python 100 Days\Day 25\weather_data.csv")
# temp_list = data["temp"].to_list()

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# faran = monday_temp * 9/5 + 32
# print(faran)

# max = (max(temp_list))

# print(data[data.temp == max])

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean())


data = pandas.read_csv("C:\Python\Python 100 Days\Day 25\Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


