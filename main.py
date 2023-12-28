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
from data import employees


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
