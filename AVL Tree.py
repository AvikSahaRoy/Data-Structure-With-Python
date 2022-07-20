from math import pi


class node:
    def __init__(self,k):
        self.left=None
        self.key=k
        self.bf=0
        self.right=None
        self.parent = None
        self.pivot = None

class AVL:
    def __init__(self):
        self.root=None
    
    # Insert Node ---------->
    def insert(self,k):
        n=node(k)
        if self.root==None:
            self.root=n
            n.parent = None
        else:
            t=self.root
            while(t!=None):
                prev=t
                if n.key<=t.key:
                    t=t.left
                else:
                    t=t.right
            if n.key<=prev.key:
                prev.left=n
                n.parent = prev
            else:
                prev.right=n
                n.parent = prev

        ob.BalanceFactor(self.root)
        self.flag = 0
        ob.IsBalanced(self.root)
        piv = n
        if self.flag == 1:
            print("Tree is Unbalanced")
            while (piv.bf == 0 or piv.bf  == 1 or piv.bf  == -1):
                piv = piv.parent
            print("Pivot is: ",piv.key) 

            # RR rotation and RL rotation ------>
            if n.key > piv.key:
                if n.key > piv.right.key:
                    ob.RRrotation(piv) 
                    print("RR rotation")
                else:
                    print("RL Rotation")
            # LL rotation and LR rotation ------>
            if n.key < piv.key:
                if n.key < piv.left.key:
                    ob.LLrotation(piv)
                    print("LL rotation")
                else:
                    print("LR Rotation")
      

        print("----------------->")

    # Calculate Height of the tree -------->
    def HeightTree(self,R):
        if R == None:
            return 0
        else:
            return max(ob.HeightTree(R.left),ob.HeightTree(R.right))+1
    
    # Calculate Balance Factor of the tree -------->
    def BalanceFactor(self, R):
        if R != None:
            R.bf = ob.HeightTree(R.left)-ob.HeightTree(R.right)
            
            print(R.key,"-->", R.bf)
            if R.parent != None:
                print(R.key,"Parent is: ",R.parent.key)
                
            ob.BalanceFactor(R.left)
            ob.BalanceFactor(R.right)

    def IsBalanced(self, R):
        if R != None:
            if (R.bf != 0 and R.bf != 1 and R.bf != -1):
                self.flag = 1
            else:
                ob.IsBalanced(R.left)
                ob.IsBalanced(R.right)
    
    def RRrotation(self, piv):
        if piv.parent == None:       
            self.root = piv.right 
            piv.right = piv.right.left
            self.root.left = piv
            self.root.parent = None
            self.root.left.parent = self.root
        else:
            piv.parent.right=piv.right
            piv.right=piv.right.left
            piv.parent.right.left=piv

            self.root.right.parent=self.root
            self.root.right.left.parent=self.root.right

    def LLrotation(self, piv):
        if piv.parent == None:
            self.root = piv.left
            piv.left = None
            self.root.right = piv


    def preorder(self, R):
        if R != None:
            print(R.key, end=" ")
            self.preorder(R.left)
            self.preorder(R.right)
        
if __name__=='__main__':     
    ob=AVL()

    # ob.insert(10)
    # ob.insert(20)
    # ob.insert(30)
    # ob.insert(40)
    # ob.insert(50)
    # ob.insert(60)
    # ob.insert(70)
    # ob.insert(80)

    ob.insert(80)
    ob.insert(70)
    ob.insert(60)
    ob.preorder(ob.root)
    # ob.insert(40)


