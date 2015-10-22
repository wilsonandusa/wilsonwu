void BST::insert(treeNode*croot,const K &  key , const D & data){
if(croot == NULL)
croot = new TreeNode(key, data);
else if(croot->key == key)
  insert(croot->left, key data);
else if(key<croot->key)
  insert(croot->left,key,data);
else
  insert(croot->right,key,data);
}      
