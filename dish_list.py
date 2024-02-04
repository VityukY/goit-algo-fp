items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algo(items, budget):
    dish_list = []
    items = items.copy()

    for name, data in items.items():
        benefit = data["calories"] / data["cost"]
        items[name]["benefits"] = benefit

    ranked_food = dict(
        sorted(items.items(), key=lambda item: item[1]["benefits"], reverse=True)
    )
    for food, data in ranked_food.items():

        if budget >= data["cost"]:
            dishes = budget // data["cost"]
            dish_list.append({food: dishes})
            budget -= data["cost"] * dishes

    if not dish_list:
        return "Треба більше золота."
    else:
        return dish_list


greedy_result = greedy_algo(items, 150)
print(f"Greedy result: {greedy_result}")


def dynamic_programming(items, budget):
    n = len(items)
    dp = [0] * (budget + 1)
    choices = [{} for _ in range(budget + 1)]

    for i in range(1, budget + 1):
        for j in range(n):
            item = list(items.keys())[j]
            cost = items[item]["cost"]
            calories = items[item]["calories"]

            if cost <= i and dp[i - cost] + calories > dp[i]:
                dp[i] = dp[i - cost] + calories
                choices[i] = {
                    **choices[i - cost],
                    **{item: choices[i - cost].get(item, 0) + 1},
                }

    result = {}
    for item, count in choices[budget].items():
        if count > 0:
            result[item] = count

    return result


# Виклик функції та виведення результату
dynamic_result = dynamic_programming(items, 150)
print(f"Dynamic result: {dynamic_result}")
