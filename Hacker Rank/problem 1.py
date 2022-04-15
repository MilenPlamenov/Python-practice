customers = ["Bigcorp", "Bigcorp", "Acme", "Bigcorp", "Zork", "Zork", "Abc", "Bigcorp", "Acme", "Bigcorp", "Bigcorp",
             "Zork", "Bigcorp", "Zork", "Zork", "Bigcorp", "Acme", "Bigcorp", "Acme", "Bigcorp", "Acme",
             "Littlecorp", "Nadircorp"]
n = 23

dict_of_customers = {}

for element in customers:
    if element not in dict_of_customers:
        dict_of_customers[element] = 1
    else:
        dict_of_customers[element] += 1


final_items_arr = []
for k,v in dict_of_customers.items():
    if (v / n) * 100 >= 5:
        final_items_arr.append(k)


print(sorted(final_items_arr))