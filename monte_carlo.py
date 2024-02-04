import random

default_values = {
    "2": 2.78,
    "3": 5.56,
    "4": 8.33,
    "5": 11.11,
    "6": 13.89,
    "7": 16.67,
    "8": 13.89,
    "9": 11.11,
    "10": 8.33,
    "11": 5.56,
    "12": 2.78,
}


def monte_carlo_simulation(num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    drop_result = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0,
    }

    for _ in range(num_experiments):
        # Генерація випадкових точок
        drops = [str(random.randint(1, 6) + random.randint(1, 6)) for _ in range(100)]
        # Відбір точок, що знаходяться всередині трикутника
        for drop in drops:
            drop_result[drop] += 1
    chances = {}
    N = sum(drop_result.values())
    for res in drop_result:
        chances[res] = round(drop_result[res] / N * 100, 2)
    return chances


# Кількість експериментів
num_experiments = 100
mc_chanse = monte_carlo_simulation(num_experiments)
sum = 0
for chance in mc_chanse:
    sum += round(abs(mc_chanse[chance] - default_values[chance]), 3)

with open("readme.md", "w", encoding="utf-8") as fp:

    # Заголовок таблички
    header = ["Drops", "Chances"]

    # Виведення заголовка
    fp.writelines(f"{header[0]:^10}|{header[1]:^10}\n")
    fp.writelines("-" * 21 + "\n")

    # Виведення даних
    for key, value in default_values.items():
        fp.writelines(f"{key:^10}|{value:^10}\n")

    # Виведення лінії
    fp.writelines("-" * 21 + "\n")

    fp.writelines(
        f"Загальна сума відміності дефолтних значеннях ймовірностей і ймовірностей отриманих методом монтекарло дорівнює: {sum}%"
    )
