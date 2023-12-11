with open("weather_data.csv") as data_file:
  data = data_file.readlines()
  print(data)

#-------------------------------------------
import csv

with open("wether_data.csv") as data_file:
  data = data_file.read()
  temperatures = []
  for row in data:
    if row[1] != "temp"
    temperatures.append(int(row[1]))
  print(temperatures)

#-------------------------------------------
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

# get data in column
print(data["condition"])
print(data.condition)

# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# create a dataframe from scratch
data_dict = {
  "students": ["Max", "Anna", "Nik"],
  "scores": [5, 3, 4]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
