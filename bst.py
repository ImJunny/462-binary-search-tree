import os
# NODE class
class Node:
  def __init__(self, val="None"):
    self.l = None
    self.val = val
    self.r = None

# INSERT method
def insert(root, val):
  if root is None: return Node(val)

  if val < root.val: root.l = insert(root.l, val)
  elif val > root.val: root.r = insert(root.r, val)
  else: print("Node already exists")
  return root

# DELETE method
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
      succ = succ.l
    
    if succParent != root: succParent.l = succ.r
    else: succParent.r = succ.r

    root.val = succ.val

    del succ
    return root

# TRAVERSAL methods
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

# GENERATE graphiz
def generate_dot(current_node, dot_file):
    if current_node is not None:
        if current_node.l is not None:
            dot_file.write(f"{current_node.val} -> {current_node.l.val};\n")
            generate_dot(current_node.l, dot_file)

        if current_node.r is not None:
            dot_file.write(f"{current_node.val} -> {current_node.r.val};\n")
            generate_dot(current_node.r, dot_file)

def generate_dot_file(root):
    with open("bst.dot", "w") as dot_file:
        dot_file.write("digraph BST {\n")
        generate_dot(root, dot_file)
        dot_file.write("}\n")

    os.system("dot -Tpng bst.dot -o bst.png")

# MAIN
if __name__ == "__main__":
  root = Node(int(input("Insert node: ")))
  while(True):
    print("Type insert | delete | preorder | inorder | postorder | generate | quit")
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
    elif (userInput =="generate"):
      generate_dot_file(root)
    else:
      break
