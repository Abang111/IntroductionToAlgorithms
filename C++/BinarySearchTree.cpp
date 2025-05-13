#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int k;
    TreeNode* l;
    TreeNode* r;
    TreeNode* p;

    TreeNode(int key) : k(key), l(nullptr), r(nullptr), p(nullptr) {}
};

class BinarySearchTree {
public:
    TreeNode* root;

    BinarySearchTree() : root(nullptr) {}

    void insert(int key) {
        TreeNode* node = new TreeNode(key);
        TreeNode* y = nullptr;
        TreeNode* x = root;

        while (x != nullptr) {
            y = x;
            if (node->k < x->k)
                x = x->l;
            else
                x = x->r;
        }

        node->p = y;
        if (y == nullptr)
            root = node;
        else if (node->k < y->k)
            y->l = node;
        else
            y->r = node;
    }

    void inorder_walk(TreeNode* node, vector<int>& result) {
        if (node != nullptr) {
            inorder_walk(node->l, result);
            result.push_back(node->k);
            inorder_walk(node->r, result);
        }
    }

    TreeNode* search(TreeNode* node, int key) {
        if (node == nullptr || key == node->k)
            return node;
        if (key < node->k)
            return search(node->l, key);
        else
            return search(node->r, key);
    }

    TreeNode* minimum(TreeNode* node) {
        while (node->l != nullptr)
            node = node->l;
        return node;
    }

    void transplant(TreeNode* u, TreeNode* v) {
        if (u->p == nullptr)
            root = v;
        else if (u == u->p->l)
            u->p->l = v;
        else
            u->p->r = v;
        if (v != nullptr)
            v->p = u->p;
    }

    void delete_node(TreeNode* z) {
        if (z->l == nullptr) {
            transplant(z, z->r);
        } else if (z->r == nullptr) {
            transplant(z, z->l);
        } else {
            TreeNode* y = minimum(z->r);
            if (y->p != z) {
                transplant(y, y->r);
                y->r = z->r;
                if (y->r) y->r->p = y;
            }
            transplant(z, y);
            y->l = z->l;
            if (y->l) y->l->p = y;
        }
    }
};
