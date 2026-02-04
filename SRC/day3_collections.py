#Task 1

inventory=["bananas","apples","carrots","dates"]
print(inventory)

inventory.append("eggs")
print(inventory)

inventory.remove("bananas")
print(inventory)

inventory.sort()
print(inventory)

#task 2

temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print(temperatures[0])
print(temperatures[-1])
print(temperatures)
print("afternoon temperatures",temperatures[3:6])
print("last 3 hours",temperatures[:-3])

#task 3

screen_res=(1920,1080)
print("Current Resolution:1920x1080")
screen_res[0]=1280
print("tuples cannot be changed")
