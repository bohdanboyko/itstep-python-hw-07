from datetime import datetime


# Завдання 1: Вивести поточну дату та час

def task1():
    now = datetime.now()

    print("Поточна дата та час:")
    print(now.strftime("%d.%m.%Y %H:%M:%S"))

task1()


# Завдання 2: Перевірити, чи є введена дата коректною

def task2():
    date_string = input(
        "Введіть дату у форматі дд.мм.рррр: "
    )

    try:
        date = datetime.strptime(date_string, "%d.%m.%Y")
        print(
            f"Дата {date.strftime('%d.%m.%Y')} є коректною."
        )
    except ValueError:
        print("Помилка: введена дата некоректна.")

task2()


# Завдання 3: Функція для визначення віку

def calculate_age(birth_date):
    today = datetime.now().date()

    age = today.year - birth_date.year

    # Якщо день народження цього року ще не настав
    if (today.month, today.day) < (
        birth_date.month,
        birth_date.day
    ):
        age -= 1

    return age


def task3():
    date_string = input(
        "Введіть дату народження (дд.мм.рррр): "
    )

    try:
        birth_date = datetime.strptime(
            date_string,
            "%d.%m.%Y"
        ).date()

        age = calculate_age(birth_date)

        if age < 0:
            print("Дата народження не може бути в майбутньому.")
        else:
            print(f"Ваш вік: {age} років")

    except ValueError:
        print("Помилка: некоректна дата.")


task3()


# Завдання 4: Різниця між двома датами

def task4():
    first_string = input(
        "Введіть першу дату (дд.мм.рррр): "
    )

    second_string = input(
        "Введіть другу дату (дд.мм.рррр): "
    )

    try:
        first_date = datetime.strptime(
            first_string,
            "%d.%m.%Y"
        )

        second_date = datetime.strptime(
            second_string,
            "%d.%m.%Y"
        )

        difference = abs(second_date - first_date)

        print(
            f"Різниця між датами: "
            f"{difference.days} днів"
        )

    except ValueError:
        print("Помилка: одна або обидві дати некоректні.")

task4()


# Завдання 5: Привітання залежно від часу доби

def get_greeting(current_time):
    hour = current_time.hour

    if 5 <= hour < 12:
        return "Доброго ранку"
    elif 12 <= hour < 18:
        return "Доброго дня"
    elif 18 <= hour < 23:
        return "Доброго вечора"
    else:
        return "Доброї ночі"


def task5():
    current_time = datetime.now()

    greeting = get_greeting(current_time)

    print(greeting + "!")

task5()


# Завдання 6: Перетворення рядка на datetime

def string_to_datetime(date_string):
    return datetime.strptime(
        date_string,
        "%d.%m.%Y"
    )


def task6():
    date_string = input(
        "Введіть дату у форматі дд.мм.рррр: "
    )

    try:
        date = string_to_datetime(date_string)

        print("Дата успішно перетворена.")
        print(f"Об'єкт datetime: {date}")

    except ValueError:
        print("Помилка: некоректний формат дати.")

task6()


# Завдання 7: Скільки днів залишилося до заданої дати

def task7():
    date_string = input(
        "Введіть майбутню дату (дд.мм.рррр): "
    )

    try:
        target_date = datetime.strptime(
            date_string,
            "%d.%m.%Y"
        ).date()

        today = datetime.now().date()

        days_left = (target_date - today).days

        if days_left > 0:
            print(
                f"До {target_date.strftime('%d.%m.%Y')} "
                f"залишилося {days_left} днів."
            )
        elif days_left == 0:
            print("Ця дата сьогодні!")
        else:
            print(
                f"Ця дата вже минула "
                f"{abs(days_left)} днів тому."
            )

    except ValueError:
        print("Помилка: некоректна дата.")

task7()

