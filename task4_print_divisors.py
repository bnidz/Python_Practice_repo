#task4 - Print divisors of the entered Number

number = input("Give a number ")
number = int(number)
#x = range(1, number)

for x in range(1, number):
    if number % x == 0:
        print(x)
