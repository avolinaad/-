name = "поставьте 10"
second_name = "пожалуйста"
year = 2003

print(name, second_name, year)

name, second_name = second_name, name
year += 60 

print(name, second_name, year)
