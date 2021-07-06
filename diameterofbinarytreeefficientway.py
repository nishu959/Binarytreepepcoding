
class btree():
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left
   
  

class pair():
  def __init__(self, node, state):
    self.state = state
    self.node = node


class diaht():
  def __init__(self, dia=0, height=0):
    self.dia = dia
    self.height = height
    
    
    
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



def diameter(root):
  if(root ==None):
    p = diaht(0,-1)
    return p
   
  a = diameter(root.left)
  b = diameter(root.right)
  
  temp = diaht()
  
  temp.height = max(a.height, b.height) + 1
 
  f = a.height + b.height + 2
  temp.dia = max(f, max(a.dia, b.dia) )
  
  
  return temp



print(diameter(root).dia)