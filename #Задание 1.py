#Задание 1
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Введите число: "))
factorial_n = factorial(n)
factorials_list = [factorial(i) for i in range(factorial_n, 0, -1)]

print("Факториал числа", n, "=", factorial_n)
print("Список факториалов:", factorials_list)
