from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'

print(message)


def calculate_square_root(Number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float) -> str:
    """Проверяет значение переменной, должно быть больше 0."""
    res_sqrt = 0
    if your_number <= 0:
        return
    else:
        res_sqrt = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. \
Это будет: {res_sqrt}')


calc(25.5)
