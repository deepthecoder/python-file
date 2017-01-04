//Author: Shubharthi Dey
//Example of Linked List
class list(object):
    def __init__(self,data,next):
    self.data=data
    self.next=None
    
class LinkedList(object):
    start=None
    end=None
    
    def insert_end(self,data):         //to insert a node in the end 
        temp=list(data,None)
        if self.start==None:
            self.start=self.end=temp
        else:
            self.end.next=node
            
   def insert_front(self,data):        //to insert a node at the beginning
       temp=list(data,None)
       if self.start==None:
            self.start=self.end=temp
       temp.next=self.start
       self.start=temp
       
   def remove_in_between(self,value):   //to remove a particular node identified by its value
       curr=self.start
       prev=None
       while curr.data is not value:
           prev=curr
           curr=curr.next
       prev.next=curr.next
       curr.next=None
  
  def display(self):                    //displaying the contents of the linked list
      curr=self.start
      while curr is not None:
          print curr.data,"->",
          curr=curr.next
      print None
  
x=LinkedList()
print("Enter 1 for insert at front , 2 for insert at end, 3 for delete in between, 4 for display")
n=input()
while(n is not 5):
    if n==1:
        y=input("Enter the node value")
        x.insert_front(y)
    if n==2:
        y=input()
        x.inert_end(y)
    if n==3:
        y=input("Insert value to delete")
        x.remove_in_between(y)
    if n==4:
        x.display()
