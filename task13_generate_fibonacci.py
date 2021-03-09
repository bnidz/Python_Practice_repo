#task13 generate fibonacci

count = int(input("How many fibonacci numbers to generate? "))
print(count)
numbers = []

numbers.append(1)
numbers.append(1)
#The sequence looks like this: 1, 1, 2, 3, 5, 8,
for i in range(2, int(count)):
    numbers.append(numbers[-1] + numbers[-2])

print(numbers)
