from sre_constants import RANGE


nest_list = [[76, 94, 29],
            [55, 43, 98],
            [74, 23, 88]]

print(nest_list[1])

for item in nest_list:
    for number in item:
        print(number)

for row_number in range(len(nest_list)):
    print(f"Row {row_number + 1} Values\n---------")
    for column_value in range(len(nest_list[row_number])):
        print(f"Column {column_value}: {nest_list[row_number][column_value]}")


print("\nTuple Demo")
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
for item in this_tuple:
    print(item)

print("\nSet Demo")
thisset = {"apple", "banana", "cherry"}

print(thisset)

