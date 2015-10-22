void BST<K>::remove(treeNode* & cRoot, const K & k){
  if(cRoot!=NULL){
  if(cRoot->key == k)
  doRemoval(cRoot);
  else if (k<croot->key)
  remove(cRoot->left,k);
  else
  remove(cRoot->right,k);
}
}

void BST<K>::doRemoval (treeNode* & cRoot){
  if((cRoot->left==NULL))&&(cRoot->right==NULL)
  noChildRemove(cRoot);
  else if((cRoot->left!=NULL)&&)(cRoot->right!=NULL)
  twoChildRemove(cRoot);
  else
  oneChildRemove(cRoot);
}

void BST<K>:::noChildRemove(treeNode* & cRoot){
  treeNode* temp = cRoot;
  cRoot=NULL;
  delete temp;
}

void BST<K>::oneChildRemove(treeNode* & cRoot){
  treeNode* temp = cRoot;
  if(cRoot->left==NULL) cRoot = cRoot->right;
  else cRoot = cRoot->left;
  delete temp;
}

void BST<k>::twoChildeRemove (treeNode * & cRoot){
  treeNode* & iop = rightMostChild(cRoot->left);
  cRoot->key = iop -> key;
  doRemoval(iop);
}

treeNode * & BST<k>::rightmostChild(treeNode* & cRoot){
  if(cRoot->right == NULL) returm cRoot;
  else return rightMostChild(cRoot->right);
}
