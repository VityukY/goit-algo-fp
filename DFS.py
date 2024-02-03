from collections import deque
from colorise import darken_hex_color


def dfs_recursive(root, queue, color_list=[], visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        global visited_list
        visited_list = []
        visited = set()
        color_list.append(root.color)
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return visited_list

    # Вилучаємо вершину з початку черги
    root_id = queue.popleft()
    current_root = root.find_node(root_id)

    # Перевіряємо, чи відвідували раніше дану вершину
    if root_id not in visited:
        # Додаємо вершину до множини відвіданих вершин.
        current_root.color = darken_hex_color(color_list[-1])
        color_list.append(current_root.color)
        print(f"after {color_list}")
        visited.add(root_id)
        visited_list.append(root_id)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        if current_root.right is not None:
            queue.appendleft(current_root.right.id)
        if current_root.left is not None:
            queue.appendleft(current_root.left.id)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    return dfs_recursive(root, queue, color_list, visited)
