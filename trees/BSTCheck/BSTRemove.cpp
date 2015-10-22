void BST<K>::remove(treeNode* & cRoot, const K & k){
  if(cRoot!=NULL){
  if(croot->key == k)
  doRemoval(cRoot);
  else if (k<croot->key)
  remove(cRoot->left,k);
  else
  remove(cRoot->right,k);
}
}
