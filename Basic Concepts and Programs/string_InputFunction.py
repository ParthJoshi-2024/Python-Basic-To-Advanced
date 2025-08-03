# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name: ")
print(f"Good Afternoon {name}!")

"""Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>"""

letter_template = '''
Dear <|Name|>,
You are selected!
<|Date|>'''
name = input("Enter your name: ")
date = input("Enter the date: ")
filled_letter = letter_template.replace("<|Name|>", name).replace("<|Date|>", date)
print(filled_letter)

# Write a program to detect double space in a string.
def detect_double_space(string):
    if "  " in string:
        return "Double space detected."
    else:
        return "No double space detected."
    
input_string = input("Enter a string: ")
result = detect_double_space(input_string)
print(result)

"""Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry, this python course is nice. Thanks!"
"""
letter = "Dear Harry, this python course is nice. Thanks!"
formatted_letter = letter.replace(" ", "\n")
print(formatted_letter)

