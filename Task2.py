foods = ("apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry")
calories = ("52 kcal", "96 kcal", "62 kcal", "605 kcal", "33 kcal", "68 kcal", "50 kcal", "33 kcal")

print(f"{foods[0]} - ({calories[0]})")
print(f"{foods[1]} - ({calories[1]})")
print(f"{foods[2]} - ({calories[2]})")
print(f"{foods[3]} - ({calories[3]})")
print(f"{foods[4]} - ({calories[4]})")
print(f"{foods[5]} - ({calories[5]})")
print(f"{foods[6]} - ({calories[6]})")
print(f"{foods[7]} - ({calories[7]})")

foods_list = list(foods)                # converts to list
calories_list = list(calories)

print(foods_list[4], calories_list[4])    # 5th item
print(foods_list[-2], calories_list[-2])  # second last item

unique_foods = set(foods_list)            #prints unique foods
print(unique_foods)

food_dict = {}                           # reates dictionary
for i in range(len(foods_list)):
    if foods_list[i] not in food_dict:
        food_dict[foods_list[i]] = calories_list[i]

print(food_dict)