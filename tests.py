from pset4 import *
import unittest

class Test_OrderedList(unittest.TestCase):

    """ test Node """

    def test_Node_init(self):
        node = Node("data")
        self.assertEqual(node.item, "data")
        self.assertEqual(node.prev, None)
        self.assertEqual(node.next, None)

    """ test OrderedList """

    def test_OrderedList_init(self):
        o_list = OrderedList()
        self.assertEqual(o_list.head, None)

    def test_OrderedList_add_0(self):
        o_list = OrderedList()
        
        o_list.add(0)
        
        self.assertEqual(o_list.head.prev, None)
        self.assertEqual(o_list.head.item, 0)
        self.assertEqual(o_list.head.next, None)

    def test_OrderedList_add_ordered(self):

        o_lst = OrderedList()
       
        for data in range(0, 11): 
            o_lst.add(data)

        current = o_lst.head
        
        act_lst = []

        while current != None:
            if current.prev == None:
                act_lst.append((current.prev, current.item, current.next.item))
            elif current.next == None:
                act_lst.append((current.prev.item, current.item, current.next))
            else:
                act_lst.append((current.prev.item, current.item, current.next.item))
            current = current.next

        exp_lst = []

        for data in range(0, 11):
            if data == 0:
                exp_lst.append((None, data, data+1))
            elif data == 10:
                exp_lst.append((data-1, data, None))
            else:
                exp_lst.append((data-1, data, data+1))

        self.assertEqual(act_lst, exp_lst)


    def test_OrderedList_add_unordered(self):

        o_lst = OrderedList()
        
        o_lst.add(1)
        o_lst.add(3)
        o_lst.add(5)
        o_lst.add(7)
        o_lst.add(9)
        o_lst.add(0)
        o_lst.add(2)
        o_lst.add(4)
        o_lst.add(6)
        o_lst.add(8)
        o_lst.add(10)

        current = o_lst.head
        
        act_lst = []

        while current != None:
            if current.prev == None:
                act_lst.append((current.prev, current.item, current.next.item))
            elif current.next == None:
                act_lst.append((current.prev.item, current.item, current.next))
            else:
                act_lst.append((current.prev.item, current.item, current.next.item))
            current = current.next

        exp_lst = []

        for data in range(0, 11):
            if data == 0:
                exp_lst.append((None, data, data+1))
            elif data == 10:
                exp_lst.append((data-1, data, None))
            else:
                exp_lst.append((data-1, data, data+1))

        self.assertEqual(act_lst, exp_lst)

    def test_OrderedList_display_None(self):
        o_lst = OrderedList()
        self.assertEqual(o_lst.display(), "[(None)]")
        
        o_lst.add(0)
        
        exp_str = "[(None 0 None)]"
        self.assertEqual(o_lst.display(), exp_str)

        o_lst.add(1)
        o_lst.add(2)

        exp_str = ("[(None 0 1)\n"
                   "(0 1 2)\n"
                   "(1 2 None)]")
        self.assertEqual(o_lst.display(), exp_str)

    def test_OrderedList_remove_None(self):
        
        o_lst = OrderedList()
        act_bool = o_lst.remove(0)
        self.assertEqual(act_bool, False)

    def test_OrderedList_remove(self):
        
        o_lst = OrderedList()
        self.assertFalse(o_lst.remove(0))
        o_lst.add(0)
        o_lst.remove(0)
        self.assertEqual(o_lst.head, None)

        o_lst.add(0)
        o_lst.add(1)
        o_lst.add(2)
        o_lst.add(3)
        o_lst.add(4)

        self.assertFalse(o_lst.remove(5))
        self.assertTrue(o_lst.remove(0))
        self.assertTrue(o_lst.remove(1))
        self.assertTrue(o_lst.remove(2))
        self.assertTrue(o_lst.remove(3))
        self.assertTrue(o_lst.remove(4))
        self.assertFalse(o_lst.remove(5))

        o_lst.add(0)
        o_lst.add(1)
        o_lst.add(2)
        o_lst.add(3)
        o_lst.add(4)

        self.assertFalse(o_lst.remove(5))
        self.assertTrue(o_lst.remove(3))
        self.assertTrue(o_lst.remove(4))
        self.assertTrue(o_lst.remove(2))
        self.assertTrue(o_lst.remove(1))
        self.assertTrue(o_lst.remove(0))
        self.assertFalse(o_lst.remove(5))

    def test_OrderedList_index(self):
        o_lst = OrderedList()
        self.assertEqual(o_lst.index(0), None)
        for data in range(0, 100):
            o_lst.add(data)
        for data in range(0, 100):
            self.assertEqual(o_lst.index(data), data)
            
    def test_orderedList_index(self):
        o_lst = OrderedList()
        with self.assertRaises(IndexError):
            o_lst.pop(0)

        for data in range(0, 100):
            o_lst.add(data)
        for data in range(0, 100):
            self.assertEqual(o_lst.pop(0), data)
         
        for data in range(0, 100):
            o_lst.add(data)
        for data in range(99, -1, -1):
            self.assertEqual(o_lst.pop(data), data)

    def test_OrderedList_contains(self):
        o_lst = OrderedList()
        for data in range(0, 100):
            o_lst.add(data)
        self.assertFalse(o_lst.contains(100))
        for data in range(0, 100):
            self.assertTrue(o_lst.contains(data))

    def test_OrderedList_to_list_1(self):
        o_lst = OrderedList()
        exp_lst = []
        self.assertEqual(o_lst.to_list(), exp_lst)
        for data in range(0, 50):
            exp_lst.append(data)
            o_lst.add(data)
        self.assertEqual(o_lst.to_list(), exp_lst)  

    def test_OrderedList_to_list_2(self):
        o_lst = OrderedList()
        exp_lst = []
        self.assertEqual(o_lst.to_list(), exp_lst)
        for data in range(0, 100):
            exp_lst.append(data)
            o_lst.add(data)
        self.assertEqual(o_lst.to_list(), exp_lst)  

    def test_OrderedList_to_list_3(self):
        o_lst = OrderedList()
        exp_lst = []
        self.assertEqual(o_lst.to_list(), exp_lst)
        for data in range(0, 500):
            exp_lst.append(data)
            o_lst.add(data)
        self.assertEqual(o_lst.to_list(), exp_lst)  

    def test_orderedList_reversed_helper_1(self):
        o_lst = OrderedList()
        exp_lst = []
        for data in range(0, 100):
            o_lst.add(data)
        for data in range(99, -1, -1):
            exp_lst.append(data)
        act_lst = reversed_helper(o_lst.head)
        self.assertEqual(act_lst, exp_lst)
        
    def test_orderedList_reversed_helper_2(self):
        o_lst = OrderedList()
        exp_lst = []
        for data in range(0, 300):
            o_lst.add(data)
        for data in range(299, -1, -1):
            exp_lst.append(data)
        act_lst = reversed_helper(o_lst.head)
        self.assertEqual(act_lst, exp_lst)

    def test_orderedList_reversed_helper_3(self):
        o_lst = OrderedList()
        exp_lst = []
        for data in range(0, 500):
            o_lst.add(data)
        for data in range(499, -1, -1):
            exp_lst.append(data)
        act_lst = reversed_helper(o_lst.head)
        self.assertEqual(act_lst, exp_lst)

    def test_orderedList_to_reversed_1(self):
        o_lst = OrderedList()
        exp_lst = []
        for data in range(0, 100):
            o_lst.add(data)
        for data in range(99, -1, -1):
            exp_lst.append(data)
        act_lst = o_lst.to_reversed_list()
        self.assertEqual(act_lst, exp_lst)

    def test_orderedList_to_reversed_2(self):
        o_lst = OrderedList()
        exp_lst = []
        for data in range(0, 300):
            o_lst.add(data)
        for data in range(299, -1, -1):
            exp_lst.append(data)
        act_lst = o_lst.to_reversed_list()
        self.assertEqual(act_lst, exp_lst)

    def test_orderedList_to_reversed_3(self):
        o_lst = OrderedList()
        exp_lst = []
        for data in range(0, 500):
            o_lst.add(data)
        for data in range(499, -1, -1):
            exp_lst.append(data)
        act_lst = o_lst.to_reversed_list()
        self.assertEqual(act_lst, exp_lst)




if __name__ == "__main__":
    unittest.main()
