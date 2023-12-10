sum = 0

numbers = input("Enter a list of numbers (separated by spaces): ").split()

for num in numbers:
    num = int(num)

    if num > 0:
        sum += num

print("The sum of positive numbers is:", sum)
