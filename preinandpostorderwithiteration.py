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



def preinpost(root):
  pre = ""
  ino = ""
  post = ""
  rp = []
  a = pair(root, 1)
  rp.append(a)
 
  while(len(rp)>0):
    
    top = rp[-1]
    if(top.state == 1):
      pre += str(top.node.data) + " "
      if(top.node.left!=None):
        p = pair(top.node.left,1)
        rp.append(p)
        
      top.state += 1
    elif(top.state == 2):
      ino += str(top.node.data) + " "
      if(top.node.right!=None):
        p = pair(top.node.right,1)
        rp.append(p) 
      top.state+=1
    elif(top.state == 3):
      post += str(top.node.data) + " "
      rp.pop()
      
      
      
  print(pre)
  print(ino)
  print(post)
  
 


preinpost(root)
