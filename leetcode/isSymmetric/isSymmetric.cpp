/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(root==NULL) return true;
        isMirror(root->left,root->right);
    }
    
    bool isMirror(TreeNode*leftNode,TreeNode*rightNode){
        if(leftNode==NULL&&rightNode==NULL)
            return true;
        else if (leftNode==NULL||rightNode==NULL)
            return false;
        else
            return leftNode->val==rightNode->val&&isMirror(leftNode->left,rightNode->right)&&isMirror(leftNode->right,rightNode->left);
    }
};
