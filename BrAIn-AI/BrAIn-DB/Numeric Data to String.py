#WARNING! This code is a sample code that shows how the "Numeric Data to String" works.
import os

digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["", "hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
thousands = ["", "thousand", "million", "billion", "trillion"]

def numericdata_to_string(number):
    if number == 0:
        return "zero"

    text = ""
    number_str = str(number)
    digit_groups = (len(number_str) - 1) // 3

    for group in range(digit_groups, -1, -1):
        group_str = number_str[-3:]
        number_str = number_str[:-3]

        hundreds_digit = int(group_str) // 100
        tens_digit = (int(group_str) % 100) // 10
        ones_digit = int(group_str) % 10

        if hundreds_digit > 0:
            text += hundreds[hundreds_digit] + " "

        if tens_digit > 0:
            text += tens[tens_digit] + " "

        if ones_digit > 0:
            text += digits[ones_digit] + " "

        if group > 0 and int(group_str) > 0:
            text += thousands[group] + " "

    return text.strip()

def savedata(folder, text):
    file_path = os.path.join(folder, "TextData.txt")
    with open(file_path, "a") as file:
        file.write(f"{text}\n")
    print(f"Data ({text}) successfully saved.")

folder = input("Enter the folder where data will be saved: ")
if not os.path.exists(folder):
    os.makedirs(folder)

while True:
    try:
        number = int(input("Please enter a number: "))
        text_representation = numericdata_to_string(number)
        print(f"The number {number} is written as \"{text_representation}\".")
        savedata(folder, f"{text_representation}")
        break
    except ValueError:
        print("Incorrect input, please try again.")
