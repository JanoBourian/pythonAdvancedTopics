import datetime 

print(dir(datetime.datetime))
value_1 = "12-01-2024"
value_2 = "2024-01-12"

birthdate = datetime.datetime.strptime("2023-11-27 06:00:00", "%Y-%m-%d %H:%M:%S")
print(birthdate)

testing = datetime.datetime.strptime("2023-11-27 05:00:00", "%Y-%m-%d %H:%M:%S")
print(testing)

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))