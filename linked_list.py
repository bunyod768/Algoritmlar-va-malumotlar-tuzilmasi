class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class llist:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data) 
            temp = temp.next   
    def push(self,data):
        # list boshiga tugun qoshish
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def Addlast(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node        
    def insertAfter(self,prev_data,data):
        temp = self.head
        while temp.data != prev_data:
            temp = temp.next
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node   

    def append(self,data):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        new_node = Node(data)
        temp.next = new_node     
    def delete(self,key):
        """Listdan qiymat o'chirish"""
        # List boshini topib olamiz
        temp = self.head
        # Birinchi tugunni tekshiramiz
        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return
        # Aks holda keyingi tugunlarni qarab chiqamiz
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # Agar qiymat topilmasa
        if temp==None:
            return
        # Tugunni listdan o'chiramiz
        prev.next = temp.next
        temp = None
       



Llist = llist()
Llist.head = Node('dushanba')
Llist.head.next = Node('seshanba')
Llist.push('chorshanba')
Llist.Addlast('payshanba')
Llist.insertAfter('seshanba','chorshanba')
Llist.append('juma')
Llist.delete('chorshanba')
Llist.print()

