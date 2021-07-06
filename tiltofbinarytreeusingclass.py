

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


class fortilt():
  def __init__(self, sot=0, tilt=0):
    self.sot = sot
    self.tilt = tilt
    
  
def tiltbtree(root):
  if(root ==None):
    l = fortilt(0,0)
    return l
  
  p = tiltbtree(root.left)
  q= tiltbtree(root.right)
  
  
  temp = abs(p.sot - q.sot)
  
  t = fortilt()
  
  t.sot = p.sot + q.sot + root.data
  
  t.tilt = temp + p.tilt + q.tilt
 
  
  return t
  

print(tiltbtree(root).tilt) 



