from pset4 import *

def test_func_OrderedList():
    o_list = OrderedList()
  
    o_list.add(1)
    o_list.add(3)
    o_list.add(5)
    o_list.add(7)
    o_list.add(9)
    o_list.add(0)
    o_list.add(2)
    o_list.add(4)
    o_list.add(6)
    o_list.add(8)
    o_list.add(10)

    current = o_list.head
    result = []
    while current != None:
        if current.prev == None:
            result.append((current.prev     , current.item, current.next.item))
        elif current.next == None:
            result.append((current.prev.item, current.item, current.next     ))
        else:
            result.append((current.prev.item, current.item, current.next.item))
        current = current.next

    for set in result:
        print(set)

test_func_OrderedList()
