#Easiest way using "in"
first_string = input("Write a string with repeated characters: ")
result_string = ""

for i, character in enumerate(first_string):
    if first_string[i] not in result_string:
        result_string += first_string[i]
print(result_string)

#Long way using only nested for loops
first_string = input("\nCool, now write some other text: ")
result_string = ""
new_character = True

for i, character in enumerate(first_string):
    for j, character2 in enumerate(result_string):
        if result_string[j] == first_string[i]:
            new_character = False
            break
        else:
            new_character = True
    if new_character == True:
        result_string += first_string[i]
print(result_string)
