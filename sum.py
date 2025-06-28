def sum(values):
    total = 0
    for value in values:
        total += value
    return total


numbers = []

for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

print(f"the sum of numbers is: {sum(numbers)}")