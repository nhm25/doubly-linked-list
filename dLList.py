# CS331 Assignment 3, 02/14/2023

# In this assignment, you are asked to implement methods in DoublyLinkedList class following the design we discussed.
# Remind that, we are using a DoublyLinkedList with a sentinel head and a cursor pointer.
# The next node of the tail is the sentinel head, and the previous node of the sentinel head is the tail.

class DoublyLinkedList:

    # Please implement each of the following methods following the guide.
    # Here, I've only implemented the construction methods and the dunder __repr__ method. Do not change them.
    # Do not use other designs of a LinkedList.

    class Node:
        ####################    DO NOT CHANGE   ####################
        def __init__(self, item, prev = None, next = None):
            self.data = item
            self.prev = prev
            self.next = next

    def __init__(self):
        ####################    DO NOT CHANGE   ####################
        self.head = DoublyLinkedList.Node(None)   # Sentinel Head, do not delete or update this node.
        self.head.prev = self.head.next = self.head
        self.cursor = self.head
        self.length = 0

    def __len__(self):
        # return the number of items stored in this DoublyLinkedList (aka, the length)
        return self.length
        pass

    def prepend(self, item):
        # Insert item as a node right after the sentinel head.
        # Make sure the pointers are pointing to correct nodes.
        # Remember to increase the length of this DoublyLinkedList.
        # Don't return anything in this method.
        node = DoublyLinkedList.Node(item)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node  # note: this refers to the former node after head sentinel which would now be the
        # node that comes after this new node that was just prepended. self.head.next - original nodel; ogNode.prev must
        # be updated to point to the prepended node that now stands before it
        self.head.next = node  # the pointer 'next' of head sentinel must be updated to point to the prepended node that
        # now stands after it otherwise the order will get messed up
        self.length += 1
        pass

    def append(self, item):
        # Insert item as a node to the tail of this DoublyLinkedList
        # Make sure the pointers are pointing to correct nodes.
        # Remember to increase the length of this DoublyLinkedList.
        # Don't return anything in this method.
        node = DoublyLinkedList.Node(item)
        node.next = self.head
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        self.length += 1
        pass

    def __iter__(self):
        # This method implements "for x in DoublyLinkedList".
        # You may use a generator (with keyword "yield" ) to implement the iterator method.
        # For each node after the Sentinel Head, yield its data (instead of yielding the node itself).
        x = 0
        self.cursor = self.head.next
        while x < self.length:
            yield self.cursor.data
            self.cursor = self.cursor.next
            x += 1
        pass

    def __repr__(self):
        ####################    DO NOT CHANGE   ####################
        return "[" + ", ".join( repr(x) for x in self ) + "]"

    def cursor_set(self, index):
        assert (isinstance(index, int)) and index >= 0 and index < self.length
        # Move the cursor to the given index, where index is in range(0, self.length).
        # Don't return anything in this method.
        self.cursor = self.head
        x = 0
        while x < index:
            self.cursor = self.cursor.next
            x += 1
        self.cursor = self.cursor.next
        pass

    def cursor_get(self):
        assert self.cursor is not self.head
        # Return the data in the node where the cursor points to.
        return self.cursor.data
        pass

    def cursor_update(self, item):
        assert self.cursor is not self.head
        # Update the data in the cursor to the input item.
        # Don't return anything in this method.
        self.cursor.data = item
        pass

    def __getitem__(self, index):
        assert (isinstance(index, int))
        # This method implements "DoublyLinkedList[index]".
        # Use cursor_set(.) and cursor_get(.) to return the data in the node at index.
        self.cursor_set(index)
        return self.cursor_get()
        pass

    def __setitem__(self, index, item):
        assert (isinstance(index, int))
        # This method implements "DoublyLinkedList[index] = item".
        # Use cursor_set(.) and cursor_update(.) to update the data in the node at index to the input item.
        # Don't return anything in this method.
        self.cursor_set(index)
        self.cursor_update(item)
        pass

    def cursor_insert(self, item):
        # Insert item within a node after the cursor.
        # Move the cursor to the inserted node.
        # Remember to increase the length of this DoublyLinkedList.
        # Don't return anything in this method.
        node = DoublyLinkedList.Node(item)
        node.next = self.cursor.next
        node.prev = self.cursor
        self.cursor.next.prev = node
        self.cursor.next = node
        self.cursor = node
        self.length += 1
        pass

    def cursor_delete(self):
        assert self.cursor is not self.head and len(self) > 0
        # Delete the cursor node and let cursor.next be the new cursor.
        # Remember to decrease the length of this DoublyLinkedList.
        # Don't return anything in this method.
        self.cursor.next.prev = self.cursor.prev
        self.cursor.prev.next = self.cursor.next
        del self.cursor.prev
        self.cursor = self.cursor.next
        self.length -= 1
        pass

    def __contains__(self, item):
        # This method implements "item in DoublyLinkedList" as a Boolean.
        # Return True if item is in this DoublyLinkedList, or else return False.
        for x in self:
            if x == item:
                return True
            else:
                return False
        pass

    def __add__(self, other):
        assert(isinstance(other, DoublyLinkedList))
        # This is implementing "self + other"
        # Append the other DoublyLinkedList to the tail of this DoublyLinkedList (self).
        # Make sure that all the pointers are pointing to the correct nodes.
        # Remember to change the self.length of the updated DoublyLinkedList accordingly.
        # Don't return anything in this method, the head of the updated DoublyLinkedList is still self.head.
        for x in other:
            self.append(x)
        pass

    def remove_items(self, item):
        # Remove each node in this DoublyLinkedList containing the input item as its data.
        # If at least one node is removed, remember to decrease the length of this DoublyLinkedList.
        # Don't return anything in this method.
        self.cursor = self.head.next
        n = 0
        for x in self:
            self.cursor_set(n)
            if self.cursor.data == item:
                self.cursor_delete()
            else:
                self.cursor = self.cursor.next
            n += 1
        pass

    def reverse_list(self):
        # Reverse the order of nodes in this DoublyLinkedList.
        # For example: if you have a DoublyLinkedList = SH <-> 1 <-> 3 <-> 5,
        # after reverse_list(), you need to update it to  SH <-> 5 <-> 3 <-> 1.
        # Here, SH means the sentinel head.
        # Since you are updating this list, don't return anything in this method.
        x = 0
        self.cursor = self.head.next
        temp = self.head.prev
        while x < self.length//2:
            first = x
            last = self.length - 1 - x
            self.cursor_set(last)
            temp1 = self.cursor_get()
            self.cursor_set(first)
            temp2 = self.cursor_get()
            self.cursor_update(temp1)
            self.cursor_set(last)
            self.cursor_update(temp2)
            x += 1
        pass


########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################
list1 = DoublyLinkedList()
for x in range(1,5):
    list1.append(x)
print("Let's start with a list consists of the first four positive integers: list1 =", list1,
      ", and its length =", list1.length, "." )

for x in range(4,8):
    list1.prepend(x)
print("Then we prepend integers 7,6,5,4 to the front, and list1 =", list1, ", and its length =", list1.length, ".")

list1.remove_items(4)
print("After removing all 4's from list1, we get list1 =", list1, ", and its length =", list1.length, ".")

list1[3] = 8
print("Let's update number 1 in list1 to 8, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.data, ".")

list1.cursor_set(2)
for x in range(9,11):
    list1.cursor_insert(x)
print("Insert number 9 and 10 after number 5, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.data, ".")

list1.cursor_set(1)
for x in range(3):
    list1.cursor_delete()
print("Delete three continuous numbers starting with 6, and we get list1 =",
      list1, "; the cursor is pointing at number", list1.cursor.data, ".")

print("Does list1 contains number 5? The answer is", 5 in list1, ".")

list2 = DoublyLinkedList()
list2.cursor_insert(1)
print("Let list2 be a list containing only number 1: list2 =", list2, ".")

list2 + list1
print("If we add list1 to the tail of list2, the new list2 =", list2, ", and its length =", list2.length, ".")

list2.reverse_list()
print("Let's reverse the order of numbers in list2, we get list2 =", list2, ".")

