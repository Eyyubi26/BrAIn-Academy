#WARNING! This code is a sample code that shows how the "String Data to Numeric" works.
import os

ones = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
tens = {"ten": 10, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
hundreds = {"hundred": 100, "twohundred": 200, "threehundred": 300, "fourhundred": 400, "fivehundred": 500, "sixhundred": 600, "sevenhundred": 700, "eighthundred": 800, "ninehundred": 900}
thousands = {"thousand": 1000, "million": 1000000, "billion": 1000000000, "trillion": 1000000000000}

def stringdata_to_numeric(text):
    if text == "zero":
        return "0"

    split_text = text.split()
    number = 0
    group_count = 0

    for word in split_text:
        if word in ones:
            number += ones[word]
        elif word in tens:
            number += tens[word]
        elif word in hundreds:
            number += hundreds[word]
        elif word in thousands:
            number *= thousands[word]
            group_count += 1

    return number

def savedata(folder, data, filename):
    file_path = os.path.join(folder, filename)
    with open(file_path, "a") as file:
        file.write(f"{data}\n")
    print(f"Data ({data}) successfully saved.")

folder = input("Enter the folder where data will be saved: ")
if not os.path.exists(folder):
    os.makedirs(folder)

while True:
    text = input("Please enter some text: ")
    try:
        numeric_value = stringdata_to_numeric(text)
        print(f"The text \"{text}\" is written as the number {numeric_value}.")
        savedata(folder, f"{numeric_value}", "NumericData.txt")
    except KeyError:
        print("Incorrect text input. Please check the text and try again.")
