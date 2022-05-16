import random


class List:
    def __init__(self, head_node):
        self.head = head_node

    def get_last_elem(self):
        current_obj = self.head
        while current_obj.has_next():
            current_obj = current_obj.next
        return current_obj

    def get_elem_and_prev(self, filter_value):
        current_obj = self.head
        while current_obj.next.value != filter_value or current_obj.has_next():
            current_obj = current_obj.next
        return current_obj, current_obj.next

    def append(self, node_obj):
        last_elem = self.get_last_elem()
        last_elem.next = node_obj

    def delete(self, filter_value):
        prev_obj, obj_for_delete = self.get_elem_and_prev(filter_value)
        prev_obj.next = obj_for_delete.next

    def __repr__(self):
        """List obj: [1, 2, 3, 4]"""
        result_str = f'List obj: ['
        current_obj = self.head
        while current_obj.has_next():
            result_str += f'{current_obj.value} '
            current_obj = current_obj.next
        return result_str + ']'


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def has_next(self):
        return self.next is not None

    def get_next(self):
        return self.next

    def __repr__(self):
        return f'Value: {self.value}, next: {self.next}'


list_obj = List(Node(10, None))

for i in range(10):
    list_obj.append(Node(random.randint(0, 100), None))

print(list_obj)
