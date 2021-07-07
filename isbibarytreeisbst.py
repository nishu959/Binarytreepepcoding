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
  
def minintree(root):
  m = sys.maxsize
  if(root==None):
    return m    
  p = minintree(root.left)
  q = minintree(root.right) 
  m = max(p, q)
  if(root.data <m):
    m = root.data
  return m
  
  
def bsttree(root):
  if(root == None):
    return True  
    
  p = bsttree(root.left)
  q = bsttree(root.right) 
  
  if(p == False):
    return False
  
  if(q == False):
    return False
    
    
  if(root.data>maxintree(root.left) and root.data<minintree(root.right)):
    return True
  else:
    return False
    
  
 

if(bsttree(root)):
  print("true")
 
else:
  print("false")
 

