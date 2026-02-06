#Task 1

def calc_rectangle(length,width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area, perimeter = calc_rectangle(length, width)

print(f"Area: {area}, Perimeter: {perimeter}")

#task 2

import math_operations

print("TASK 2")
num_list=[10,22,21,11,44]
base=int(input("Enter base:"))
exp=int(input("Enter power:"))
print("Power=",math_operations.pow(base, exp))
print("Average=",math_operations.average(num_list))

    