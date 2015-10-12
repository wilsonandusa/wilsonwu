#include <iostream>

using namespace std;

class BinaryTree {
    private:
        class Node {
            public:
                int data;
                Node *left, *right;
                Node(int data, Node *left, Node *right) {
                    this->data = data;
                    this->left = left;
                    this->right = right;
                }
                ~Node() {
                    if (this->left) delete this->left;
                    if (this->right) delete this->right;
                }
        };
        Node *root;
    public:
        void populate() {
            delete root;
            root = new Node(-2,
                    new Node(-1, 
                        new Node(2,NULL,NULL),
                        new Node(1,NULL,NULL)),
                    new Node(-1, 
                        new Node(6,NULL,NULL),
                        new Node(8,NULL,NULL)));
        }

        int calc(Node *n) {
            if (n == NULL)
                return 0;
            else if (n->data >= 0)
                return n->data;
            else if (n->data == -2)
                return calc(n->left) * calc(n->right);
            else if (n->data == -1)
                return calc(n->left) + calc(n->right);
            else return 8675309;
        }
        
        int calc() {
            return calc(root);
        }


        int sum(Node *n) {
            if (n) 
                return n->data + sum(n->left) + sum(n->right);
            else
                return 0;
        }
        int sum() {
            return sum(root);
        }

        int height(Node *n) {
            if (n) 
                return 1 + max(height(n->left),
                        height(n->right));
            else
                return 0;
        }
        int height() {
            return height(root);
        }

        void preorder(Node *n) {
            if (n) {
                cout << n->data << " ";
                preorder(n->left);
                preorder(n->right);
            }
        }
        void preorder() {
            preorder(root);
        }

};

int main() {
    BinaryTree *t = new BinaryTree();

    t->populate();
    cout << t->sum() << endl;
    cout << t->calc() << endl;
}
