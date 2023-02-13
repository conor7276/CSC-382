def BST_Sum(self,root):
    def BST_Sum_Helper(root):
        if(root):
            return root.val + BST_Sum_Helper(root.left) + BST_Sum_Helper(root.right)
        else:
            return 0
    print(BST_Sum_Helper(root))


def Print_BST(self,root):
    def Print_BST_Helper(root):
        if(root):
            Print_BST_Helper(root.left)
            print(root.val)
            Print_BST_Helper(root.right)

