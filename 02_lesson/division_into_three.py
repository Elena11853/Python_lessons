#Деление на три

#Создайте функцию dev_by_three, которая принимает один аргумент — число — и возвращает 'Да', если оно делится на три, 
# и 'Нет' — если не делится.
#В этом же файле напишите код, который вызывает функцию и передает в нее число.
#Результат вызова функции должен сохраняться в переменную.
#Выведите в консоль сообщение в формате: Делится ли на три <число>? - Нет | Да

def dev_by_three(number):
    return 'Да' if number % 3 == 0 else 'Нет'
num = int(input('Введите число '))
result = dev_by_three(num)
print(f'Делится на 3 {num}? - {result}')