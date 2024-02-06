import turtle


def draw_pifagor_tree(turtle, branch_length, recursion_level):
    if recursion_level == 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(45)
        draw_pifagor_tree(turtle, 0.6 * branch_length, recursion_level - 1)
        turtle.right(90)
        draw_pifagor_tree(turtle, 0.6 * branch_length, recursion_level - 1)
        turtle.left(45)
        turtle.backward(branch_length)


def main():
    # Запитуємо користувача про рівень рекурсії
    recursion_level = int(input("Введіть рівень рекурсії: "))

    # Ініціалізуємо туртл (знімок черепашки) і встановлюємо параметри
    my_turtle = turtle.Turtle()
    my_turtle.speed(2)
    my_turtle.penup()
    my_turtle.goto(0, -200)
    my_turtle.pendown()

    # Встановлюємо початковий напрямок на 90 градусів проти годинникової стрілки
    my_turtle.left(90)

    # Викликаємо функцію для малювання дерева Піфагора з вказаним рівнем рекурсії
    draw_pifagor_tree(my_turtle, 100, recursion_level)

    # Завершуємо програму при натисканні на вікно
    turtle.exitonclick()


if __name__ == "__main__":
    main()
