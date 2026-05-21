import random

# Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


result = dict(zip(keys, values))
print(result)

# 🌟 Exercise 2: Cinemax #2

# Basic family data
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Bonus: allow user to add members (basic input, no try/except)
add_more = input("Do you want to add family members? (y/N): ").strip().lower()
if add_more == 'y':
	while True:
		name = input("Name (blank to finish): ").strip()
		if not name:
			break
		age_input = input(f"Age for {name}: ").strip()
		age = int(age_input)
		family[name] = age

# Calculate total cost and print per-person price
total_cost = 0
for name, age in family.items():
	if age < 3:
		price = 0
	elif age <= 12:
		price = 10
	else:
		price = 15
	total_cost += price
	print(f"{name.title()} pays ${price}")

print(f"Total cost: ${total_cost}")


# 🌟 Exercise 3: Zara
brand = {
	'name': 'Zara',
	'creation_date': 1975,
	'creator_name': 'Amancio Ortega Gaona',
	'type_of_clothes': ['men', 'women', 'children', 'home'],
	'international_competitors': ['Gap', 'H&M', 'Benetton'],
	'number_stores': 7000,
	'major_color': {
		'France': 'blue',
		'Spain': 'red',
		'US': ['pink', 'green']
	}
}

# Change number_stores to 2
brand['number_stores'] = 2

# Print sentence about clients
print("Zara's clients are: " + ", ".join(brand['type_of_clothes']))

# Add country_creation
brand['country_creation'] = 'Spain'

# Add Desigual to international_competitors if key exists
if 'international_competitors' in brand:
	brand['international_competitors'].append('Desigual')

# Delete creation_date
del brand['creation_date']

# Print last international competitor
print('Last international competitor:', brand['international_competitors'][-1])

# Print major colors in the US
print('Major colors in the US:', ", ".join(brand['major_color']['US']))

# Print number of keys and all keys
print('Number of keys:', len(brand))
print('Keys:', list(brand.keys()))

# Bonus: merge with more_on_zara
more_on_zara = {'creation_date': 1975, 'number_stores': 7000}
brand.update(more_on_zara)
print('Brand after merge:', brand)


# 🌟 Exercise 4: Some Geography
def describe_city(city, country='Unknown'):
	print(f"{city} is in {country}.")

describe_city('Reykjavik', 'Iceland')
describe_city('Paris')


# 🌟 Exercise 5: Random
def compare_with_random(n):
	rand = random.randint(1, 100)
	if n == rand:
		print('Success!')
	else:
		print(f'Fail! Your number: {n}, Random number: {rand}')

compare_with_random(50)


# 🌟 Exercise 6: Personalized shirts
def make_shirt(size='large', text='I love Python'):
	print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt('medium')
make_shirt('small', 'Custom message')
make_shirt(size='small', text='Hello!')


# 🌟 Exercise 7: Temperature Advice
def get_random_temp(month=None):
	# Return a floating-point temperature. If month provided, choose season ranges.
	if month is None:
		return random.uniform(-10, 40)
	month = int(month)
	# Northern hemisphere seasons approximation
	if month in (12, 1, 2):  # winter
		return random.uniform(-10, 8)
	if month in (3, 4, 5):  # spring
		return random.uniform(0, 16)
	if month in (6, 7, 8):  # summer
		return random.uniform(16, 35)
	# autumn
	return random.uniform(0, 20)

def main():
	use_month = input('Do you want to enter the month for season? (y/N): ').strip().lower()
	if use_month == 'y':
		month = int(input('Enter month (1-12): ').strip())
		temp = get_random_temp(month)
	else:
		temp = get_random_temp()
	print(f"The temperature right now is {temp:.1f} degrees Celsius.")
	if temp < 0:
		print("Brrr, that's freezing! Wear some extra layers today.")
	elif temp < 16:
		print("Quite chilly! Don't forget your coat.")
	elif temp < 23:
		print("Nice weather.")
	elif temp < 32:
		print("A bit warm, stay hydrated.")
	else:
		print("It's really hot! Stay cool.")

main()


# 🌟 Exercise 8: Pizza Toppings
toppings = []
while True:
	topping = input("Enter a topping (or 'quit' to finish): ").strip()
	if topping.lower() == 'quit':
		break
	print(f"Adding {topping} to your pizza.")
	toppings.append(topping)

base_price = 10
price_per_topping = 2.5
total = base_price + len(toppings) * price_per_topping
print('Toppings:', toppings)
print(f'Total cost: ${total:.2f}')


