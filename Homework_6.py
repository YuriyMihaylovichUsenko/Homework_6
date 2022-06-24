# Task 1
import random

random_number_set = set()
while len(random_number_set) < 10:
    random_number_set.add(random.randint(0, 100))
print(max(random_number_set))

# Task 2

list_of_10_random_integers = [random.randint(0, 10) for i in range(10)]
list_of_10_random_integers_2 = [random.randint(0, 10) for i in range(10)]
print(set(list_of_10_random_integers) & set(list_of_10_random_integers_2))

# Task 3

list_of_integers_from_1_to_100 = list(range(1, 101))
result_list = []
while len(list_of_integers_from_1_to_100) != 0:
    if list_of_integers_from_1_to_100[0] % 7 == 0 and list_of_integers_from_1_to_100[0] % 5 != 0:
        result_list.append(list_of_integers_from_1_to_100[0])
    list_of_integers_from_1_to_100.pop(0)
print(result_list)
