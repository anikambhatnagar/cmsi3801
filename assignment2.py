'''
Assignment 2

'''

#1.6 string compression

def compress_string(our_string: str) -> str:
    char_dict = dict()
    new_string = ""
    length = len(our_string)
    if length == 0:
        return ""

    count = 1

    for x in range(1, length):
        if our_string[x] == our_string[x-1]:
            count += 1
        else:
            new_string += our_string[x-1] + str(count)
            count = 1

    new_string += our_string[-1] + str(count)
    return new_string

print(compress_string("aabcccccaaa"))
print(compress_string("Aabcccccaaa"))



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

l = LinkedList()
l.append("a")
l.append("b")
l.append("c")
l.append("d")
l.append("e")

print(l.string())
delete_middle(l.head.next.next)
print(l.string())



#2.5 sum lists
