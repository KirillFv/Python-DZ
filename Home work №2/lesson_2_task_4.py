fizz_buzz = input("Введите число: ")
n = int(fizz_buzz)

for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("fizz_buzz")
        elif n % 3 == 0:
            print("fizz")
        elif n % 5 == 0:
            print("buzz")
        else:
            print(n)


            