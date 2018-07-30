# Name:            Zhoushuai (Andrew) Wu
# Course:          CPE 202
# Instructor:      Daniel Kauffman
# Assignment:      Problem Set 3: Ordered [Double Linked] List
# Term:            Summer 2018


class Node:

    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next


def display_while(current, is_head, is_tail, result_lst):
    
    while current != None:
        if is_head and current.prev == None and current.next == None:
            n_str = "(" + "None" + " " + str(current.item) + \
                " " + "None" + ")"
            is_head = False
        elif is_head and current.prev == None:
            n_str = "(" + "None" + " " + str(current.item) + \
                " " + str(current.next.item) + ")"
            is_head = False
        elif is_tail and current.next == None:
            n_str = "(" + str(current.prev.item) + " " + \
                str(current.item) + " " + "None" + ")"                
            is_tail = False
        else:
            n_str = "(" + str(current.prev.item) + " " + \
                str(current.item) + " " + str(current.next.item) + ")" 
        result_lst.append(n_str)
        current = current.next


def reversed_helper(current):
    if current == None :
        return []
    return reversed_helper(current.next) + [current.item]


class OrderedList:

    def __init__(self):
        self.head = None


    def add(self, item):
        current = self.head
        if self.head == None:                         # list is empty
            self.head = Node(item)
        elif self.head.item >= item:                   # new_node goes before first item
            new_node = Node(item, next = self.head)
            self.head.prev = new_node
            self.head = new_node
        else:
            while current.item < item:
                if current.next == None:
                    new_node = Node(item, prev = current)
                    current.next = new_node
                elif current.next.item >= item:
                    new_node = Node(item, current, current.next)
                    current.next.prev = new_node
                    current.next = new_node 
                current = current.next
            

    def remove(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.item == item:
                found = True
            else:
                current = current.next
        if not found:
            return False
        else:
            if current.prev == None and current.next == None:
                self.head = None
            elif current.prev == None and current.next != None:
                current.next.prev = None
                self.head = current.next
            elif current.prev != None and current.next != None:
                temp = current.next
                current.prev.next = temp
                temp.prev = current.prev
            elif current.prev != None and current.next == None:
                current.prev.next = None
            return True
                

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.item == item:
                found = True
            else:
                current = current.next
                index += 1
        if not found:
            return None
        else:
            return index
        


    def pop(self, index):
        current = self.head
        found = False
        c_index = 0
        while current != None and not found:
            if c_index == index:
                found = True
            else:
                current = current.next
                c_index += 1
        if not found:
            raise IndexError
        else:
            temp = current.item
            self.remove(current.item)
            return temp

    def contains(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.item == item:
                found = True
            else:
                current = current.next
        return found


    def to_list(self):
        result = []
        current = self.head
        while current != None:
            result.append(current.item)
            current = current.next
        return result


    def to_reversed_list(self):
        current = self.head
        return reversed_helper(current)


    def display(self):
        result_lst = []
        current = self.head
        is_head = True
        is_tail = True
        if current == None:
            return "[(None)]"
        display_while(current, is_head, is_tail, result_lst)
        result_str = "[" + "\n".join(result_lst) + "]"
        return result_str

