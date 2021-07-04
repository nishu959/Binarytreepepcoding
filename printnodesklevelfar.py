
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
ele= int(input())
k =int(input())

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



def nodetoroot(root, ele):
  if(root == None):
    return []
  if(root.data == ele):
    l = []
    l.append(root)
    return l
  p = nodetoroot(root.left, ele)
  if(len(p)>0):
    p.append(root)
    return p
  
  q = nodetoroot(root.right, ele)
  if(len(q)>0):
    q.append(root)
    return q
    
  return []




def printkdown(root, k, block):
  if(root == None or k<0 or block==root):
    return
    
  if(k==0):
    print(root.data)
    
  printkdown(root.left, k - 1, block)
  
  printkdown(root.right, k -1, block)
  
  return 
  
  
  

def printkfar(root, ele,k):
  ntrp = nodetoroot(root,ele)
  
  for i in range(len(ntrp)):
    
    
    printkdown(ntrp[i], k-i, ntrp[i-1] if i>0 else None)
    
    
    
    
printkfar(root, ele, k)
  
  
  
  