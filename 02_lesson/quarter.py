#Квартал

#Напишите функцию quarter_of_year(), которая принимает один аргумент — номер месяца (от 1 до 12) — и возвращает номер квартала, 
# к которому относится этот месяц.Например, если передать 5, на выходе должно быть II квартал, 
# так как май относится ковтоому кварталу.
def quarter_of_year(month):
    if 1 <= month <= 3:
        return "I квартал"
    elif 4 <= month <= 6:
        return "II квартал"
    elif 7 <= month <= 9:
        return "III квартал"
    elif 10 <= month <= 12:
        return "IV квартал"
    else:
        return "Неверный номер месяца"

try:
    month = int(input("Введите номер месяца (1-12): "))
    print(quarter_of_year(month)) 
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")