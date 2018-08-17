#python 3.5.2

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
           
    def append(self, new_data):
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
            
        last.next = new_node
   
    def deleteList(self):
        current = self.head
        
        while current:
            prev = current.next
            del current.data
            current = prev
        
            
if __name__ == '__main__':
    llist = LinkList()
    
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.printList()
    llist.deleteList()
    llist.printList()
