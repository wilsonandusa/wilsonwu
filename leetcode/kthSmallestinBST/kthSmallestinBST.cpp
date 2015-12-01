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
    int kthSmallest(TreeNode* root, int k) {
        int retVal = 0;
        kthSmallest_helper(root,k,retVal);
        return retVal;
    }
    
    void kthSmallest_helper(TreeNode* root, int &k, int &retVal){
        if(!root||k<=0)
        return ;
        //first traverse to the bottom left
        kthSmallest_helper(root->left,k,retVal);
        k--;
        if(k==0){
            retVal = root->val;
            return;
        }
        kthSmallest_helper(root->right,k,retVal);
    }
};
