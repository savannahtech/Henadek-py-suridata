# Exercise guidelines:
# 1. You will receive a template that contains a list of employees, each employee
# contains three fields.
# 2. You will need to simulate a “Dwarf-Giant” game – in case you are unfamiliar,
# the goal of the game is to create unique pairs of all employees.
# 3. Each pair includes a Dwarf and a Giant – [(dwarf1, giant1), (dwarf2, giant2), ...]
# 4. For the game to be fair, each employee needs to be a dwarf exactly one time,
# and a giant exactly one time.

# Please consider the following:
# 1. The input may include duplicates – it needs to be validated and cleaned. The
# unique index is a combination of all three fields.
# 2. The output needs to be random – each execution will need to produce a
# different output.
# 3. The combination of pairs such as (employee_1, employee_2) and (employee_2,
# employee_1) is forbidden.
# 4. For validation purposes, the output must be a single list of tuples, where the
# first element of each tuple is the dwarf’s name and the second element in a
# giant’s name (only name, not the entire object).

import random

employees = [
	{
		"department": "R&D",
		"name": "Nikolas Porter",
		"age": 46
	},
	{
		"department": "Sales",
		"name": "Sterling Walton",
		"age": 28
	},
	{
		"department": "R&D",
		"name": "Louis Mcintosh",
		"age": 33
	},
	{
		"department": "R&D",
		"name": "Joyce Randolph",
		"age": 29
	},
	{
		"department": "R&D",
		"name": "Oliver Mcconnell",
		"age": 63
	},
	{
		"department": "Support",
		"name": "Jimena Roman",
		"age": 22
	},
	{
		"department": "Support",
		"name": "Ellis Davenport",
		"age": 25
	},
	{
		"department": "Sales",
		"name": "Jorge Good",
		"age": 29
	},
	{
		"department": "R&D",
		"name": "Sasha Horn",
		"age": 50
	},
	{
		"department": "Sales",
		"name": "Aracely Nguyen",
		"age": 63
	},
	{
		"department": "Support",
		"name": "Kenyon York",
		"age": 71
	},
	{
		"department": "R&D",
		"name": "Oliver Mcconnell",
		"age": 63
	},
	{
		"department": "Sales",
		"name": "Saniyah Luna",
		"age": 27
	},
	{
		"department": "R&D",
		"name": "Abigayle Sosa",
		"age": 29
	},
	{
		"department": "R&D",
		"name": "Elisha Andrade",
		"age": 24
	},
	{
		"department": "Sales",
		"name": "Abril Schaefer",
		"age": 22
	},
	{
		"department": "R&D",
		"name": "Katrina Hanna",
		"age": 21
	},
	{
		"department": "R&D",
		"name": "Kaiya Fry",
		"age": 28
	},
	{
		"department": "R&D",
		"name": "Shyann Harmon",
		"age": 33
	},
	{
		"department": "R&D",
		"name": "Darnell Rangel",
		"age": 31
	},
	{
		"department": "R&D",
		"name": "Kendall Cochran",
		"age": 37
	},
	{
		"department": "R&D",
		"name": "Kylan Cantrell",
		"age": 28
	},
	{
		"department": "R&D",
		"name": "Amiah Powell",
		"age": 29
	},
	{
		"department": "R&D",
		"name": "Maria Kelley",
		"age": 22
	},
	{
		"department": "R&D",
		"name": "Jay Gonzales",
		"age": 43
	},
	{
		"department": "R&D",
		"name": "Shea Robles",
		"age": 29
	},
	{
		"department": "R&D",
		"name": "Kenyon Patel",
		"age": 23
	},
	{
		"department": "Support",
		"name": "Esmeralda Harris",
		"age": 33
	},
	{
		"department": "Sales",
		"name": "Donovan Petersen",
		"age": 23
	},
	{
		"department": "Sales",
		"name": "Ralph Yu",
		"age": 25
	},
	{
		"department": "R&D",
		"name": "Nadia Hernandez",
		"age": 26
	},
	{
		"department": "Support",
		"name": "Finley Vang",
		"age": 27
	},
	{
		"department": "R&D",
		"name": "Kelvin Cameron",
		"age": 44
	},
	{
		"department": "Support",
		"name": "Zack Barnes",
		"age": 23
	},
	{
		"department": "R&D",
		"name": "Evelyn Roth",
		"age": 23
	},
	{
		"department": "Sales",
		"name": "Charlize Cobb",
		"age": 47
	},
	{
		"department": "Sales",
		"name": "Devin Benitez",
		"age": 23
	},
	{
		"department": "R&D",
		"name": "Jaidyn Noble",
		"age": 70
	},
	{
		"department": "Sales",
		"name": "Jaydin Braun",
		"age": 63
	},
	{
		"department": "Sales",
		"name": "Anthony Bray",
		"age": 51
	},
	{
		"department": "Sales",
		"name": "Leila Becker",
		"age": 55
	},
	{
		"department": "R&D",
		"name": "Simon Walker",
		"age": 57
	},
	{
		"department": "R&D",
		"name": "Alan Kemp",
		"age": 22
	},
	{
		"department": "R&D",
		"name": "Elliot Cantu",
		"age": 23
	},
	{
		"department": "Support",
		"name": "Fiona Pearson",
		"age": 25
	},
	{
		"department": "Sales",
		"name": "Clara Bradley",
		"age": 23
	},
	{
		"department": "R&D",
		"name": "Aimee Mcpherson",
		"age": 38
	},
	{
		"department": "R&D",
		"name": "Quinn Reese",
		"age": 43
	},
	{
		"department": "Sales",
		"name": "Houston Nguyen",
		"age": 33
	},
	{
		"department": "Support",
		"name": "Jayleen Henry",
		"age": 37
	},
	{
		"department": "Sales",
		"name": "Terrance Gallagher",
		"age": 23
	},
	{
		"department": "R&D",
		"name": "Axel Bolton",
		"age": 23
	},
	{
		"department": "Sales",
		"name": "Dario Robertson",
		"age": 23
	},
	{
		"department": "Sales",
		"name": "Nadia David",
		"age": 82
	},
	{
		"department": "Support",
		"name": "Grayson Barrera",
		"age": 30
	},
	{
		"department": "Support",
		"name": "Lillie Pollard",
		"age": 30
	},
	{
		"department": "R&D",
		"name": "Desiree Carey",
		"age": 30
	},
	{
		"department": "R&D",
		"name": "Jaden Hardin",
		"age": 30
	},
	{
		"department": "Sales",
		"name": "Jason Jimenez",
		"age": 30
	},
	{
		"department": "Sales",
		"name": "Jordyn May",
		"age": 32
	},
	{
		"department": "Sales",
		"name": "Alvaro Haley",
		"age": 33
	},
	{
		"department": "Sales",
		"name": "Zackary Nguyen",
		"age": 54
	},
	{
		"department": "Support",
		"name": "Lilliana Wood",
		"age": 42
	},
	{
		"department": "Support",
		"name": "Koen Luna",
		"age": 24
	},
	{
		"department": "Sales",
		"name": "Taniyah Ramos",
		"age": 21
	},
	{
		"department": "Sales",
		"name": "Messiah Glover",
		"age": 20
	},
	{
		"department": "R&D",
		"name": "Jazmine Massey",
		"age": 29
	},
	{
		"department": "Support",
		"name": "Carolina Rowe",
		"age": 28
	},
	{
		"department": "Sales",
		"name": "Heaven Bartlett",
		"age": 26
	},
	{
		"department": "Sales",
		"name": "Harry Peterson",
		"age": 44
	},
	{
		"department": "Sales",
		"name": "Francisco Escobar",
		"age": 69
	},
	{
		"department": "Support",
		"name": "Brendon Osborne",
		"age": 65
	},
	{
		"department": "Support",
		"name": "Yuram Henson",
		"age": 55
	},
	{
		"department": "R&D",
		"name": "Lindsey Hines",
		"age": 48
	},
	{
		"department": "R&D",
		"name": "Brayden Young",
		"age": 35
	},
	{
		"department": "Support",
		"name": "Rhianna Potter",
		"age": 30
	},
	{
		"department": "Support",
		"name": "June Hanna",
		"age": 19
	},
	{
		"department": "R&D",
		"name": "Eli Buck",
		"age": 20
	},
	{
		"department": "R&D",
		"name": "Shayna Burke",
		"age": 65
	},
	{
		"department": "Support",
		"name": "Kristopher Sanders",
		"age": 62
	},
	{
		"department": "R&D",
		"name": "Tate Yates",
		"age": 52
	},
	{
		"department": "Sales",
		"name": "Hayden Massey",
		"age": 50
	},
	{
		"department": "R&D",
		"name": "Grady Baird",
		"age": 51
	},
	{
		"department": "Sales",
		"name": "Dalia Gomez",
		"age": 44
	},
	{
		"department": "Support",
		"name": "Riley Fowler",
		"age": 48
	},
	{
		"department": "R&D",
		"name": "Madilyn Melton",
		"age": 37
	},
	{
		"department": "R&D",
		"name": "Omar Browning",
		"age": 39
	},
	{
		"department": "R&D",
		"name": "Melody Nielsen",
		"age": 44
	},
	{
		"department": "R&D",
		"name": "Camron Jacobs",
		"age": 30
	},
	{
		"department": "R&D",
		"name": "Royce Moore",
		"age": 41
	},
	{
		"department": "Support",
		"name": "Ariel Reed",
		"age": 42
	},
	{
		"department": "Support",
		"name": "Yuram Henson",
		"age": 55
	},
	{
		"department": "Sales",
		"name": "Kaleb Benitez",
		"age": 51
	},
	{
		"department": "Sales",
		"name": "Mariyah Park",
		"age": 52
	},
	{
		"department": "Sales",
		"name": "Saige Castro",
		"age": 40
	},
	{
		"department": "Sales",
		"name": "Kristin Dorsey",
		"age": 61
	},
	{
		"department": "Support",
		"name": "Reed Parks",
		"age": 62
	},
	{
		"department": "R&D",
		"name": "Gerald Booker",
		"age": 43
	},
	{
		"department": "Support",
		"name": "Bennett Wolf",
		"age": 23
	},
	{
		"department": "Support",
		"name": "Abby Zuniga",
		"age": 30
	},
	{
		"department": "R&D",
		"name": "Vaughn Phelps",
		"age": 19
	},
	{
		"department": "R&D",
		"name": "Aditya Wilkerson",
		"age": 27
	},
	{
		"department": "Support",
		"name": "Jadon Tucker",
		"age": 26
	},
	{
		"department": "Sales",
		"name": "Erica Bullock",
		"age": 34
	},
	{
		"department": "Sales",
		"name": "Wilson Medina",
		"age": 36
	},
	{
		"department": "Support",
		"name": "Justice Boyle",
		"age": 37
	},
	{
		"department": "Support",
		"name": "Mina Caldwell",
		"age": 44
	}
]


def data_cleaning(input_data: list[dict]) -> list[dict]:
	"""
	Data cleaning of input data list
	Duplicates are removed on attributes:  'name',  'age', 'department'
	"""
	unique_employees = []
	unique_combinations = set()
	for employee in input_data:
		index = (employee['name'], employee['age'], employee['department'])
		if index not in unique_combinations:
			unique_employees.append(employee)
			unique_combinations.add(index)
	return unique_employees


def random_pair_gen(employee_list: list[dict]) -> list[tuple]:
	"""
		Shuffling, splitting 50:50 and Generate unique employee pairs
	"""
	# Shuffle the employee list
	random.shuffle(employee_list)

	# Split employees into dwarfs and giants
	split_5050 = int(len(employee_list) * 0.5)
	dwarfs = employee_list[:split_5050]
	giants = employee_list[split_5050:]

	# Generate unique pairs of dwarfs and giants
	dg_pairs = []
	for dwarf, giant in zip(dwarfs, giants):
		dg_pairs.append((dwarf['name'], giant['name']))

	return dg_pairs


def dwarf_giant_combination_check(dwarf_giant: list) -> list[tuple]:
	"""
		Check the combination of pairs like:
		(employee_1, employee_2) and (employee_2, employee_1)
		isn't allowed
	"""
	validated_pairs = []
	used = set()
	for pair in dwarf_giant:
		pair_set = frozenset(pair)
		if pair_set not in used:
			validated_pairs.append(pair)
			used.add(pair_set)
	return validated_pairs


def run() -> list[tuple]:
	cleaned_employees = data_cleaning(employees)
	dwarf_giant_pairs = random_pair_gen(cleaned_employees)
	validated_pairs = dwarf_giant_combination_check(dwarf_giant_pairs)

	return validated_pairs


if __name__ == '__main__':
	print(run())
