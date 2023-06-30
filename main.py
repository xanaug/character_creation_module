from random import randint

DEFAULT_ATTACK = 5  # глобальная константа стандартного урона
DEFAULT_DEFENCE = 10  # глобальная константа стандартной защиты
DEFAULT_STAMINA = 80


# Объявляем родительский класс для всех персонажей - Warrior, Mage и Healer.
class Character:
    # Константа для диапазона очков урона.
    RANGE_VALUE_ATTACK = (1, 3)
    # Константа для диапазона очков защиты (переменная класса).
    RANGE_VALUE_DEFENCE = (1, 5)
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    SPECIAL_SKILL = 'Удача'  # название умения
    SPECIAL_BUFF = 15  # значение очков урона для базового класса

    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки, используется встроенная библиотека #random или константа.
    def attack(self):
        # Описываем метод атаки.
        # 1 вариант
        # return (f'{self.name} нанёс противнику урон, равный '
        #         f'{5 + randint(5, 10)}')
        # 2 вариант (без использования глобальной константы)
        # value_attack = 5 + randint(*self.RANGE_VALUE_ATTACK)
        # return (f'{self.name} нанёс противнику урон, равный {value_attack}')
        # 3 вариант (вместо числа 5 теперь используется константа DEFAULT_ATTACK)
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}.')

    # Объявляем метод защиты.
    def defence(self):
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())

# Вывод в терминал:
# Warrior — дерзкий воин ближнего боя. Сильный, выносливый и отважный.
# Кодослав нанёс урон противнику, равный 8


game_classes = {
    'warrior': Warrior,
    'mage': Mage,
    'healer': Healer,
}


def start_training(character):
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special,
    }
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Замените блок условных операторов на словарь
        # и вынесите его из цикла. Здесь останется одно условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        if cmd in commands:
            print(commands[cmd])
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = None

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

