class btree():
  def __init__(self, data, right=None, left=None):
    self.data =data
    self.right = right
    self.left = left
   
  

class pair():
  def __init__(self, node, state):
    self.state = state
    self.node = node




n = [50,25,12,None, None, 37,30,None, None, None, 75,62,None,70,None,None,87,None,None]


root = btree(n[0])

stack = []
p = pair(root, 1)
stack.append(p)

idx = 0

while(len(stack)>0):
  top = stack[-1]
  if(top.state == 1):
    
    idx+=1
    if(n[idx]!=None):
      t = btree(n[idx])
      top.node.left = t
      
      p = pair(t, 1)
      stack.append(p)
    else:
      top.node.left = None
      
    top.state += 1
    
    
  elif(top.state == 2):
    idx+=1
    if(n[idx]!=None):
      t = btree(n[idx],None, None)
      top.node.right = t
      
      p = pair(t, 1)
      stack.append(p)
    else:
      top.node.right = None
      
    top.state += 1
     
  else:
    stack.pop()




def display(root):
  if(root == None):
    return
  s = ""
  s += str(root.left.data) if (root.left!=None) else "."
  
  s += "<-" + str(root.data) + "->" 
  
  s += str(root.right.data) if (root.right!=None) else "."
 
  print(s)
  
  display(root.left)
  display(root.right)
       

    
display(root)
  

  
  




