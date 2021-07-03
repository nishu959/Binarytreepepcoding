
import sys


class btree():
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left
   
  

class pair():
  def __init__(self, node, state):
    self.state = state
    self.node = node

m = int(input())
n = list(map(str, input().split()))

def btreeform(n, s, root):
  
  root = btree(int(n[0]))
  
  
  p = pair(root,1)
  s.append(p)
  idx =0
  while(len(s)>0):
    top = s[-1]
    if(top.state == 1):
    
      idx+=1
      if(n[idx]!="n"):
        t = btree(int(n[idx])) 
        top.node.left = t
      
        p = pair(t, 1)
        s.append(p)
      else:
        top.node.left = None
      
      top.state += 1
    
    
    elif(top.state == 2):
      idx+=1
      if(n[idx]!="n"):
        t = btree(int(n[idx]) ,None, None)
        top.node.right = t
      
        p = pair(t, 1)
        s.append(p)
      else:
        top.node.right = None
      
      top.state += 1
     
    else:
      s.pop()


  return root
  
  
root = btreeform(n, [], None)


def size(root):
  if(root ==None):
    return 0
  p = size(root.left)
  q = size(root.right)
  return p+q+1
        
        
print("Size =", size(root)) 

def sumoftree(root):
  if(root ==None):
    return 0
   
  p = sumoftree(root.left)
  q = sumoftree(root.right)
  ans = p +q + root.data
  
  return ans
  
  
  
print("Sum of tree =", sumoftree(root))


def maxintree(root):
  m = -1*sys.maxsize
  if(root==None):
    return m    
  p = maxintree(root.left)
  q = maxintree(root.right) 
  m = max(p, q)
  if(root.data >m):
    m = root.data
  return m
  
  
  
  
 
  
print("Maximum in tree =", maxintree(root)) 


def height(root):
  if(root == None):
    return -1
  p = height(root.left)
  q = height(root.right)
  ht = max(p, q)
  return ht+1
  
  
print("Height of tree =", height(root))
     
        
        
  
  