
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
low= int(input())
high=int(input())

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

#Adtiya Verma recursion


def ptlfr(root,strpath, low, high, stp):
  if(root==None):
    return
  
  if(root.left == None and root.right == None):
    if(stp>= low and stp<=high):
      print(strpath)
  op1l = strpath+str(root.left.data)+" " if (root.left!=None) else strpath+""
  op2l = stp+root.left.data if (root.left!=None) else stp+0
  
  op1r = strpath+str(root.right.data)+" " if (root.right!=None) else strpath+""
  op2r = stp+root.right.data if (root.right!=None) else stp+0
  
  ptlfr(root.left,op1l, low, high, op2l)
  ptlfr(root.right,op1r, low, high, op2r)
  
  

ptlfr(root, str(root.data)+ " ", low, high, root.data)


