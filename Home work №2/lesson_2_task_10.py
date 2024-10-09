
# сумма вклада/ расчет под 10% годовых
def bank(X , Y):
    rate = 0.10
    sum_after_y_years = X * (1 + rate) ** Y
    return sum_after_y_years
    

X = int(input(" Введите сумму: "))

Y = int(input(" Какой срок? "))

# Ответ

result = bank(X, Y)
print(f"Если вы внесете {X} на {Y} года, то на вашем счете будет {result:.2f} ")