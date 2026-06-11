n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

print("Sum =", sum(numbers))