def sigma(numbers):
    diff = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i-1] != diff:
            return False
    return True

numbers = [1, 3, 5, 7, 9]
result = sigma(numbers)
print(result)
