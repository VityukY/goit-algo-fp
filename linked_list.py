class Node:
    def __init__(self, data=None, sorted=False):
        self.data = data
        self.next = None
        self.sorted = sorted


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

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        unsorted_head = self.head
        while unsorted_head:
            current = unsorted_head
            unsorted_head = unsorted_head.next

            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and current.data > temp.next.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

        self.head = sorted_head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


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


def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    list1.insertion_sort()
    list2.insertion_sort()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data <= current2.data:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

    while current1:
        merged_list.insert_at_end(current1.data)
        current1 = current1.next

    while current2:
        merged_list.insert_at_end(current2.data)
        current2 = current2.next

    return merged_list


if __name__ == "__main__":
    llist = LinkedList()

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    llist.display()
    llist.insertion_sort()
    llist.display()

    reverse_list(llist)
    print("reverse linked list")
    llist.display()

    llist2 = LinkedList()

    llist2.insert_at_beginning(6)
    llist2.insert_at_beginning(11)
    llist2.insert_at_beginning(16)
    llist2.insert_at_end(21)
    llist2.insert_at_end(26)
    merged_list = merge_sorted_lists(llist, llist2)
    merged_list.display()
