name = input("enter your name: ")
age = input("enter your age: ")
current_age=input("what is your current age: ")
current_age=int(current_age)
age_2030=current_age+4
print(f"hey {name}, you will be {age_2030} in 2030!: ")

num_people=input("Enter number of people: ")
total=input("total bill amount: ")
num_people=int(num_people)
total=int(total)
billperperson=total/num_people
print(type(num_people))
print(type(total))
print(type(billperperson))
print(f"totalbill={total}. Each person pays: {billperperson}: ")

item_name = "socks"
quantity = 5
price=150
in_stock=True
print(f" Item : {item_name} Qyt : {quantity} Price : {price} Available : {in_stock}")
print(item_name)
print(quantity)
totalbill_cost=quantity*price
print("total cost:", totalbill_cost)

    