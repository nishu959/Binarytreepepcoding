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

class levelpair():
  def __init__(self, pointer, level):
    self.pointer = pointer
    self.level = level

def levelorder(root):
  s = []
  p = levelpair(root, 0)
  s.append(p)
  ls = 0
  while(len(s)>0):
    a = s.pop(0)
    if a.pointer!=None:
      if(a.level > ls):
        ls = a.level
        print()
       
      print(a.pointer.data, end = " ")
      
        
      t = levelpair(a.pointer.left,ls+1)
      q = levelpair(a.pointer.right,ls+1)
      s.append(t) 
      s.append(q)
  
levelorder(root)