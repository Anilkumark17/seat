class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
            
class LinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        new_node= Node(data)
        
        if self.head is None:
            self.head=new_node
        else:
            last= self.head
            while last.next:
                last=last.next
            last.next=new_node  
            
    def search(self,target):
         
        position=0
        current=self.head
        
       
        while(current):
            if current.data==target:
                return position
            
            current=current.next
            position=position+1
        position=-1
            
        
                                
                    
            
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # To indicate the end of the linked list

# Create the linked list and append elements
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

# Display the linked list
ll.display()

# Perform a linear search
target = 30
position = ll.search(target)

if position != -1:
    print(f"Element {target} found at position {position}.")
else:
    print(f"Element {target} not found in the linked list.")
