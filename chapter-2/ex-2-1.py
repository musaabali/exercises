# Programming Exercise 2-1
# 
# Program to display one person's contact information.
# This program needs no input
# and performs no computations.
# It will display the name and contact information for a teacher.

name ="Musaab Ali"
address = "555 Milbury Lane"
city = "Coralville, IA, 52241"
phone = "319-123-4567"
area ="CIS-121"
def print_address(full_name,address,city_state_zip,phone,area):
	print(full_name)
	print(address)
	print(city_state_zip)
	print(phone)
	print(area)

print_address(name, address, city, phone, area)
