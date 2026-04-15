class node:
    def __init__(self,mydata):
        self.data = mydata
        self.leftChild = None
        self.rightChild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def TreeBnaKrDo(self):
        NameOfChild = input("Name of Child: ")
        myChild = node(NameOfChild)

        if myChild == "Uday":
            return None
        
        print("left Child name: ",myChild)
        myChild.leftChild = self.TreeBnaKrDo()
        print("right Child name: ",myChild)
        myChild.rightChild = self.TreeBnaKrDo()

        return myChild 


    
