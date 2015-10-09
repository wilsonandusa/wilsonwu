template <typename T>
bool BinaryTree<T>::isOrdered() const
{
    return isOrdered(root);
    cout<<endl;
}

template <typename T>
bool BinaryTree<T>::isOrdered(const Node*subtree)const
{	bool inorder = true;
    if (subtree==NULL)
    return true;

	if (subtree->left!= NULL)
	{
		if (subtree->elem < maxonleft(subtree->left))
		{
			inorder = false;
		}
	}
	if (subtree->right!=NULL)
	{
		if (subtree->elem > minonright(subtree->right))
		{
			inorder = false;
		}
	}
	return (inorder&&isOrdered(subtree->left)&&isOrdered(subtree->right));
}

template <typename T>
T BinaryTree<T>::maxonleft(const Node*subtree)const
{
	if (subtree->left==NULL&&subtree->right==NULL)
	return subtree->elem;
	
	else if (subtree->left!=NULL&&subtree->right == NULL)
	{
		return max(subtree->elem,maxonleft(subtree->left));
	}
	else if (subtree->left==NULL&&subtree->right!=NULL)
	{
		return max(subtree->elem,maxonleft(subtree->right));
	}
	else return max(subtree->elem,max(maxonleft(subtree->left),maxonleft(subtree->right)));


}
template <typename T>
T BinaryTree<T>::minonright(const Node*subtree)const
{
	if (subtree->left==NULL&&subtree->right==NULL)
	return subtree->elem;
	
	else if (subtree->left!=NULL&&subtree->right == NULL)
	{
		return min(subtree->elem,minonright(subtree->left));
	}
	else if (subtree->left==NULL&&subtree->right!=NULL)
	{
		return min(subtree->elem,minonright(subtree->right));
	}
	else return min(subtree->elem,min(minonright(subtree->left),minonright(subtree->right)));
}
/**
