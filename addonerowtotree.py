
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth ==1:
            a = TreeNode(val)
            a.left = root
            return a
        
        l = []
        l.append(root)
        while(depth>2):
            depth -= 1
            temp = []
            while(len(l)!=0):
                rem = l.pop(0)
                if rem.left!=None:
                    temp.append(rem.left)
                if rem.right!=None:
                    temp.append(rem.right)
            l = temp
            
            
            
        while(len(l)!=0):
            top = l.pop(0)
            temp1 = top.left
            temp2 = top.right
            s = TreeNode(val)
            t = TreeNode(val)
            top.left = s
            top.right = t
            s.left = temp1
            t.right = temp2
            
        return root