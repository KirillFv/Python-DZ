
def is_year_leap(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Введите год: "))


if is_year_leap(year):
    print(f"год {year}: True — Это високосный год!")
else:
    print(f"год {year}: False — Это не високосный год!")



