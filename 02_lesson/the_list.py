#Дан список 
#lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
#Необходимо вывести элементы, которые одновременно: больше 15, делятся на 3 без остатка.
lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
result = [x for x in lst if x > 15 and x % 3 == 0]
print(result)