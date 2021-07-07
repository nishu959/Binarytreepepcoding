
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


class balance():
  def __init__(self, tf=True, ht = -1):
    self.tf = tf
    self.ht= ht
    
    

def isbalan(root):
  if(root == None):
    b = balance(True, -1) # 0 will also work checking balance
    return b
    
  p = isbalan(root.left)
  q = isbalan(root.right)
  
 
  l = balance()
  
  
 
  
  temp = (p.tf and q.tf) #for checking other tree follow balance
  
  a  = abs(p.ht - q.ht) #for checking this node follow balance or not
  ans = True
  if(a>1):
    ans = False
  
  l.tf = temp and ans #if both follow then balanced tree
  
  """
  THIS WORK IS DONE IN SINGLE LINE IN AND p.ht etc... 
  
  if(p.ht==False):
    l.ht = False
  
  if(q.ht==False):
    l.ht = False
    
  """
  
  l.ht = max(p.ht,q.ht) +1
  
  
  return l
  
  
if(isbalan(root).tf):
  print("true")
else:
  print("false")
  
  
  
  