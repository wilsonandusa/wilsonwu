//In-Order Traversal 
// visit the left branch, then the current node, and finally, the right branch
void inOrderTraversal(TreeNode node){
  if(node != NULL){
  inOrderTraversal(node.left);
  visit(node);
  inOrderTraversal(node.right);
  }
}
// it visits the nodes in ascending order

//Pre-Order Traversal: visit the current node before its child nodes 
void PreorderTraversal(TreeNode node){
  if(node != NULL){
    visit(node);
    PreorderTraversal(node.left)
    PreorderTraversal(node.right);
  }
}

//Post Order Traversal, visit the current node after its child nodes
void postordertraversal(TreeNode node){
  if(node != NULL){
    postorderTraversal(node.left)
    postorderTraversal(node.right);
    visit(node);
  }
}
