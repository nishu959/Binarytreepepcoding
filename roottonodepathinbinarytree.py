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
ele = int(input())

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





def ispath(root, ele):
  if (root == None):
    return False
  if(root.data == ele):
    return True

  p = ispath(root.left, ele)
  if(p == True):
    return True
    
  q = ispath(root.right, ele)
  if(q == True):
    return True
    
  return False


if(ispath(root, ele)):
  print("true")
else:
  print("false")
  
  
 
def nodetoroot(root, ele):
  if(root == None):
    return []
  if(root.data == ele):
    l = []
    l.append(ele)
    return l
  p = nodetoroot(root.left, ele)
  if(len(p)>0):
    p.append(root.data)
    return p
  
  q = nodetoroot(root.right, ele)
  if(len(q)>0):
    q.append(root.data)
    return q
    
  return []


print(nodetoroot(root,ele))



