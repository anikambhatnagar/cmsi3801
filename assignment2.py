'''
Assignment 2

'''

#1.6 string compression

def compress_string(our_string: str) -> str:
    char_dict = {}
    new_string = ""

    for char in our_string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    keys_list = list(char_dict.keys())
    for key in keys_list:
        new_string += key
        new_string += str(char_dict[key])
    return new_string
'''
print(compress_string("aabcccccaaa"))
print(compress_string("Aabcccccaaa"))
print(compress_string("aabccbcccaaa"))
'''



#2.3 delete middle node
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def delete(self, data):
        temp = self.head
        while temp.next != None:
            #if its what we are looking for,
            if temp.next.data == data:
                #delete it
                temp.next = temp.next.next
            temp = temp.next
    def string(self):
        s = ""
        temp = self.head
        while temp != None:
            s += temp.data
            s += " -> "
            temp = temp.next
        s += "|"
        return s

def delete_middle(node):
    #delete given node from its linked list
    temp = node
    while temp != None:
        temp.data = temp.next.data
        if temp.next.next == None:
            temp.next = None
        temp = temp.next
'''
l = LinkedList()
l.append("a")
l.append("b")
l.append("c")
l.append("d")
l.append("e")

print(l.string())
delete_middle(l.head.next.next)
print(l.string())
'''

#2.5 sum lists
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def append(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def string(self):
        s = ""
        temp = self.head
        while temp != None:
            s += temp.data
            s += " -> "
            temp = temp.next
        s += "|"
        return s

def sum_linked_lists(l1, l2):
        num1 = ""
        num2 = ""
        #if in reversed order:
        '''
        for node in l1:
            num1 = node + num1
        for node in l2:
            num2 = node + num2
        '''
        #if in normal order:
        for node in l1:
            num1 += node
        for node in l2:
            num2 += node
        sum = int(num1) + int(num2)
        sum_list = LinkedList()
        for num in str(sum):
            sum_list.append(node)
        ans = str_to_linked_list(str(sum))
        return ans.string()

def str_to_linked_list(str: str) -> LinkedList:
    l1 = LinkedList()
    for char in str:
        l1.append(char)
    return l1

'''
l1 = LinkedList()
l2 = LinkedList()
#reverse order
l1.append("7")
l1.append("1")
l1.append("6")
l2.append("5")
l2.append("9")
l2.append("2")

#normal order
l1.append("6")
l1.append("1")
l1.append("7")
l2.append("2")
l2.append("9")
l2.append("5")

print(l1.string())
print(l2.string())
print(sum_linked_lists(l1, l2))
'''

#3.2 stack min
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            top_element = self.items[-1]
            self.items = self.items[:-1]
            return top_element
        else:
            raise IndexError("Stack is empty.")

    def min(self):
        if not self.is_empty():
            min_val = self.items[0]
            for item in self.items:
                if item < min_val:
                    min_val = item
            return min_val
        else:
           raise ValueError("Stack is empty.")
    
    def string(self):
        my_string = f''
        for item in self.items:
            temp = str(item)
            my_string += f'{temp} '
        return my_string
'''
s1 = Stack()
s1.push(0)
s1.push(10)
s1.push(-20)
s1.push(5)
s1.pop()
print(s1.string())
print(s1.min())
'''

#3.3 stack of plates
class SetOfStacks:
    def __init__(self):
        self.items = Stack()
         