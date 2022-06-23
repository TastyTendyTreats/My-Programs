sentnce = "The quick brown fox jumps over the lazy dog."
print(sentnce.lower())
print(sentnce.upper())

print("\nEndswith")
file_name = "numbers"
if not file_name.endswith(".txt"):
    file_name = file_name + ".txt"
print(file_name)

print("\nString concatenation")
first_name = "Kristofferson"
last_name = "Culmer"
full_name = first_name + " " + last_name
print(full_name)

print("\nString Indexes")
print(full_name[5])
for letter in full_name:
    print(letter)

print("\nString Slicing")
#print up to a specified index
print(full_name[0:5])
#print from a specified index until the end of the string
print(full_name[13:])
#reverse a string
print(full_name[::-1])

print("\nMore String concatenation")
character = "*"
print(character*5)

stop_value = 10
for number_of_stars in range(1,stop_value + 1):
    print((" " * (stop_value - number_of_stars)) + (character * (number_of_stars))) 

# user input  == "y" or user_input == "Y"
user_input = input("To continue enter Y")
if user_input.upper() == "Y":
    print("Yes you may continue")
else:
    print("Goodbye")

