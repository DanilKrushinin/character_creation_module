from random import randint

# Вот она — новая глобальная константа.
# Атака для спец умения
DEFAULT_ATTACK = 5

# Защита для спец умения
DEFAULT_DEFENCE = 10

# Выностивость для спец умения
DEFAULT_STAMINA = 80


# Поместите сюда код объявленных классов.
class Character:
    # Характеристики родительского класса
    # Диапазон атаки
    RANGE_VALUE_ATTACK = (1, 3)
    # Жиапазон защиты
    RANGE_VALUE_DEFENCE = (1, 5)
    # Урон для базового класса
    SPECIAL_BUFF = 15
    # Названия спец умения
    SPECIAL_SKILL = 'Удача'
    # Новая константа
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name
        pass

    # Описание класса атака
    def attack(self):
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный '
                f'{value_attack}')

    # Описание класса отражение удара
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    # Описание класса спец атака
    def special(self):
        # Здесь описано тело метода special().
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    # Описание персонажа
    # Новый метод базового класса.
    # __class__.__name__ - вывести имя у объекта класса есть специальный атрибут
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.' 


# Описание класса Воин. 
class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


# Описание класса Маг. 
class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


# Описание класса Лекарь
class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """

    # Добавили словарь, в котором соотносится ввод пользователя и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str  = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    # Замените конструкцию условных операторов на словарь.
    commands = {'attack': Character.attack(),
                'defence': Character.defence(),
                'special': Character.special()
                }
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands.keys():
        # Вместо блока условных операторов добавьте условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
            print(commands(cmd))
    return 'Тренировка окончена.'



##################################################################################################################################################
########################################Предыдущая версия#########################################################################################
##################################################################################################################################################

# from random import randint

# # Новый импорт.
# # Из модуля start_game_banner, который расположен в папке graphic_arts,
# # импортируем функцию run_screensaver().
# from graphic_arts.start_game_banner import run_screensaver


# def attack(char_name: str, char_class: str) -> str:
#     """Расчет уровня нанесенного урона."""
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон противнику равный \
#             {5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон противнику равный \
#             {5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон противнику равный \
#             {5 + randint(-3, -1)}')


# def defence(char_name: str, char_class: str) -> str:
#     """Расчет уровня блокировки урона."""
#     if char_class == 'warrior':
#         return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
#     if char_class == 'mage':
#         return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
#     if char_class == 'healer':
#         return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


# def special(char_name: str, char_class: str) -> str:
#     """Расчет уровня специальной атаки."""
#     if char_class == 'warrior':
#         return (f'{char_name} применил специальное умение \
#             «Выносливость {80 + 25}»')
#     if char_class == 'mage':
#         return (f'{char_name} применил специальное умение \
#             «Атака {5 + 40}»')
#     if char_class == 'healer':
#         return (f'{char_name} применил специальное умение \
#             «Защита {10 + 30}»')


# def start_training(char_name: str, char_class: str) -> str:
#     """Тренировка выбранного персонажа."""
#     if char_class == 'warrior':
#         print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
#     if char_class == 'mage':
#         print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
#     if char_class == 'healer':
#         print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
#     print('Потренируйся управлять своими навыками.')
#     print('Введи одну из команд: attack — чтобы атаковать противника, \
#         defence — чтобы блокировать атаку противника \
#             или special — чтобы использовать свою суперсилу.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     cmd: str = None
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd == 'attack':
#             print(attack(char_name, char_class))
#         if cmd == 'defence':
#             print(defence(char_name, char_class))
#         if cmd == 'special':
#             print(special(char_name, char_class))
#     return 'Тренировка окончена.'


# def choice_char_class() -> str:
#     """Выбор персонажа."""
#     approve_choice: str = None
#     char_class: str = None
#     while approve_choice != 'y':
#         char_class = input('Введи название персонажа, \
#             за которого хочешь играть: Воитель — warrior, \
#                 Маг — mage, Лекарь — healer: ')
#         if char_class == 'warrior':
#             print('Воитель — дерзкий воин ближнего боя. \
#                 Сильный, выносливый и отважный.')
#         if char_class == 'mage':
#             print('Маг — находчивый воин дальнего боя. \
#                 Обладает высоким интеллектом.')
#         if char_class == 'healer':
#             print('Лекарь — могущественный заклинатель. \
#                 Черпает силы из природы, веры и духов.')
#         approve_choice = input('Нажми (Y), чтобы подтвердить выбор, \
#             или любую другую кнопку, чтобы выбрать другого персонажа ').lower()
#     return char_class


# # def main() -> None:
# if __name__ == '__main__':
#     run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name: str = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class: str = choice_char_class()
#     print(start_training(char_name, char_class))


# # main()
