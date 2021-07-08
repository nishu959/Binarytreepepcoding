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


  
bolans = True

 
def bsttree(root):
  global bolans
  if(root == None):
    return [sys.maxsize,-1* sys.maxsize]
    
  p = bsttree(root.left)
  q = bsttree(root.right) 
 
  temp = [min(min(p[0], q[0]) ,root.data), max(max(q[1],p[1]),root.data)]
  
  
  if(root.data>= p[1] and root.data <= q[0]):
    pass
  else:
    ans = False
    bolans = ans
    
    
 
  
  return temp
  
    
bsttree(root)

print("true") if(bolans) else print("false")
  
    
  
 