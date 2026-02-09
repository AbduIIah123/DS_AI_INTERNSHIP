#task 1
with open("journal.txt","a") as file:
    r=input("Your name and today's goal:")
    file.write("\n"+r)

with open("journal.txt","r") as file:
    r=file.read()
    print(r)
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
