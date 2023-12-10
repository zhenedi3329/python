age = int(input("Enter your age: "))

if age <= 13:
    print("You belong to the children age group.")
elif age <= 21:
    print("You belong to the teenagers age group.")
elif age <= 59:
    print("You belong to the adulthood age group.")
else:
    print("You belong to the old age group.")
