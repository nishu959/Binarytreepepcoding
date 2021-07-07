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


def height(root):
  
  if(root == None):
    return -1
  p = height(root.left)
  q = height(root.right)
  ht = max(p, q)
  return ht+1


def isbalan(root):
  if(root == None):
    return True
  p = isbalan(root.left)
  if(p==False):
    return False
    
  q = isbalan(root.right)
  if(q==False):
    return False
    
    
  a= abs(height(root.left) - height(root.right)) 
  if(a<=1):
    return True
  else:
    return False
    
    

if(isbalan(root)):
  print("true")
else:
  print("false")



  
  
  

  
  