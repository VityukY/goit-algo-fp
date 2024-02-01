class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    # llist.delete_node(10)

    def reverse_list(llist):
        current_node = llist.head.next
        llist.head.next = None
        prev_node = llist.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        llist.head = prev_node

    reverse_list(llist)
    print("reverse linked list")
    llist.print_list()

    def insert_sort(list_data):
        """сортує отриманий список методом вставки"""
        for i in range(1, len(list_data)):
            key = list_data[i]
            j = i - 1
            while j >= 0 and key < list_data[j]:
                list_data[j + 1] = list_data[j]
                j -= 1
            list_data[j + 1] = key
        return list_data

    def get_llist_data(llist):
        """отримує значення всіз елементів звязного списку"""
        curr_node = llist.head
        llist_data = []
        while curr_node:
            llist_data.append(curr_node.data)
            curr_node = curr_node.next
        return llist_data

    def list_sorting(llist):
        """вивантажує зі списку всі значення, сортує їх і вставляє у той самий список, замінючи тільки значення у вузлах, зберігаючи порядок"""
        llist_data = get_llist_data(llist)
        for i in range(1, len(llist_data)):
            key = llist_data[i]
            j = i - 1
            while j >= 0 and key < llist_data[j]:
                llist_data[j + 1] = llist_data[j]
                j -= 1
            llist_data[j + 1] = key
        counter = 0
        llist.head.data = llist_data[counter]
        next_node = llist.head.next
        while next_node:
            counter += 1
            next_node.data = llist_data[counter]
            next_node = next_node.next

    list_sorting(llist)
    print("Sorted (insert method)")
    llist.print_list()

    llist_2 = LinkedList()

    # Вставляємо вузли в початок
    llist_2.insert_at_beginning(4)
    llist_2.insert_at_beginning(11)
    llist_2.insert_at_beginning(13)
    llist_2.insert_at_end(21)
    llist_2.insert_at_end(23)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist_2.print_list()
    list_sorting(llist_2)
    print("second list sorted")
    llist_2.print_list()

    def llist_merge(llist, llist2):
        """бере всі дані з двох списків, обєднює і сортує їх, створю новий звязний список, наповнює відсортованими даними новий список"""
        llist_data = get_llist_data(llist)
        llist2_data = get_llist_data(llist2)
        llist_data.extend(llist2_data)
        sorted_llist_data = insert_sort(llist_data)
        merged_llist = LinkedList()
        for i in sorted_llist_data:
            merged_llist.insert_at_end(i)
        return merged_llist

    merget_list = llist_merge(llist, llist_2)
    print("Merged sorted list")
    merget_list.print_list()
