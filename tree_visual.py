import uuid
from BFS import bfs_recursive
from DFS import dfs_recursive
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:

    def __init__(self, key, color="#0f4138"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def find_node(self, target_id):
        list = [self]

        while list:
            current_node = list.pop()

            if current_node.id == target_id:
                return current_node

            if current_node.right:
                list.append(current_node.right)
            if current_node.left:
                list.append(current_node.left)

        return None


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree):
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


bfs_recursive(root, deque([root.id]))
tree = nx.DiGraph()
pos = {root.id: (0, 0)}
tree = add_edges(tree, root, pos)
draw_tree(tree)

dfs_recursive(root, deque([root.id]))
tree_two = nx.DiGraph()
pos = {root.id: (0, 0)}
tree_two = add_edges(tree, root, pos)
draw_tree(tree_two)
