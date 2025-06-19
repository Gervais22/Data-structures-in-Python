item1Cost = 20.5
item2Cost = 15.0
item3Cost = 10.0

total = 0

answer = input("Did you buy any of item 1? (Yes/No): ")
if answer.lower() == "yes":
    quantity = int(input("How many did you buy? "))
    total += quantity * item1Cost

answer = input("Did you buy any of item 2? (Yes/No): ")
if answer.lower() == "yes":
    quantity = int(input("How many did you buy? "))
    total += quantity * item2Cost

answer = input("Did you buy any of item 3? (Yes/No): ")
if answer.lower() == "yes":
    quantity = int(input("How many did you buy? "))
    total += quantity * item3Cost

print("Your total is", total)
