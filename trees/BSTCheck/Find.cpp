TreeNode* BST Find(treeNode* croot, const K & key){
  if(croot == NULL)
  return NULL;
  else if (croot->key == key){
  return croot;}
  else if (key < croot ->key)
  return find(croot->left, key);
  else
  return find(croot->right. key); 
}
