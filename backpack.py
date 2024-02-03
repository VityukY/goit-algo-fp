items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algo(items, budget):
    backpack = []
    items = items.copy()

    for name, data in items.items():
        benefit = data["calories"] / data["cost"]
        items[name]["benefits"] = benefit

    ranked_food = dict(
        sorted(items.items(), key=lambda item: item[1]["benefits"], reverse=True)
    )
    print(ranked_food)
    for food, data in ranked_food.items():

        if budget >= data["cost"]:
            dishes = budget // data["cost"]
            backpack.append({food: dishes})
            budget -= data["cost"] * dishes

    if not backpack:
        return "Треба більше золота."
    else:
        return backpack


print(greedy_algo(items, 333))
