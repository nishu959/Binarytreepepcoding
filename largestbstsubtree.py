

  
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

class btisbst():
  def __init__(self, tf=True, mxm=-1*sys.maxsize , mim=sys.maxsize, larroot=None, size=0):
    self.tf = tf
    self.mxm = mxm
    self.mim = mim
    self.larroot = larroot
    self.size = size
 
  
  
  
def bsttree(root):
  if(root == None):
    
    p = btisbst(True, -1*sys.maxsize , sys.maxsize, None, 0)
    return p
    
  p = bsttree(root.left)
  q = bsttree(root.right) 
 
  
  l = btisbst()
  l.tf = p.tf and q.tf and (root.data >= p.mxm and root.data <= q.mim)
  
  l.mxm = max(root.data,max(p.mxm,q.mxm))
  l.mim = min(root.data,min(p.mim,q.mim))
  
  if(l.tf):
    l.larroot = root
    l.size = p.size + q.size + 1
  
  else:
    if(p.size > q.size):
      l.larroot = p.larroot
      l.size = p.size
    else:
      l.larroot = q.larroot
      l.size = q.size
  
  return l
  
    
  

p = bsttree(root) 
print(p.larroot.data,p.size, sep ="@")
  
  
