#task 1

name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Daily Goal: {goal}\n")

print("Entry saved!")

#task 2

import csv
with open("student.csv","r") as file:
    reader = csv.DictReader(file)

    print("Students who passed:")
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
            
#task 3
try:
    with open("config.txt","r") as file:
        file.read()
except FileNotFoundError:
    print("file does not exist")
