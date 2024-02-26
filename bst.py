class Node:
  def __init__(self, val="None"):
    self.l = None
    self.val = val
    self.r = None

def insert(root, val):
  if root is None: return Node(val)

  if val < root.val: root.l = insert(root.l, val)
  elif val > root.val: root.r = insert(root.r, val)
  else: print("Node already exists")
  return root

def delete(root, val):
  if root is None: return root
  
  if val < root.val:
    root.l = delete(root.l, val)
    return root
  elif val > root.val:
    root.r = delete(root.r, val)
    return root
  
  if root.l is None:
    temp = root.r
    del root
    return temp
  elif root.r is None:
    temp = root.l
    del root
    return temp
  else:
    succParent = root
    succ = root.r
    while succ.l is not None:
      succParent = succ
      succ = succ.left
    
    if succParent != root: succParent.l = succ.r
    else: succParent.r = succ.r

    root.val = succ.val

    del succ
    return root
  
def preorder(root):
  if root:
    print(root.val, end=" ")
    preorder(root.l)
    preorder(root.r)

def inorder(root):
  if root:
    inorder(root.l)
    print(root.val, end=" ")
    inorder(root.r)

def postorder(root):
  if root:
    postorder(root.l)
    postorder(root.r)
    print(root.val, end=" ")

if __name__ == "__main__":
  root = Node(int(input("Insert node: ")))
  while(True):
    print("Type insert | delete | preorder | inorder | postorder | quit")
    userInput = input("Input: ")

    if (userInput == "insert"): root = insert(root, int(input("Insert node: ")))
    elif (userInput == "delete"): root = delete(root, int(input("Delete node: ")))
    elif (userInput == "preorder"):
      preorder(root)
      print()
    elif (userInput == "inorder"):
      inorder(root)
      print()
    elif (userInput =="postorder"):
      postorder(root)
      print()
    else:
      break