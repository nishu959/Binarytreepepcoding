# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        ans = self.depth(root)
        l = []
        for i in range(ans):
            if i%2==0:
                l.append(-sys.maxsize)
            else:
                l.append(sys.maxsize)
        level = 0
        res = self.dfs(root, l, level)
        return res
        
        
    def dfs(self, root, l, level):
        if root == None:
            return True
        if level %2==0:
            if root.val % 2 == 0:
                return False
            if root.val <= l[level]:
                return False
            
            l[level] = root.val
        else:
            if root.val % 2 != 0:
                return False
            if root.val >= l[level]:
                return False
        
            l[level] = root.val
        
        ansleft = self.dfs(root.left, l, level +1 )
        ansright = self.dfs(root.right,l, level+1)
        
        if ansleft == False:
            return False
        if ansright == False:
            return False
        
        return True
        
    def depth(self, root):
        if root == None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1