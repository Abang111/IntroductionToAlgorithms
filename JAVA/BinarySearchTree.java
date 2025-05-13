
    import java.util.*;

    class TreeNode {
        int k;
        TreeNode l, r, p;

        TreeNode(int key) {
            this.k = key;
            this.l = this.r = this.p = null;
        }
    }

    public class BinarySearchTree {
        TreeNode root = null;

        public void insert(int key) {
            TreeNode node = new TreeNode(key);
            TreeNode y = null;
            TreeNode x = root;

            while (x != null) {
                y = x;
                if (node.k < x.k)
                    x = x.l;
                else
                    x = x.r;
            }

            node.p = y;
            if (y == null)
                root = node;
            else if (node.k < y.k)
                y.l = node;
            else
                y.r = node;
        }

        public void inorderWalk(TreeNode node, List<Integer> result) {
            if (node != null) {
                inorderWalk(node.l, result);
                result.add(node.k);
                inorderWalk(node.r, result);
            }
        }

        public TreeNode search(TreeNode node, int key) {
            if (node == null || key == node.k)
                return node;
            if (key < node.k)
                return search(node.l, key);
            else
                return search(node.r, key);
        }

        public TreeNode minimum(TreeNode node) {
            while (node.l != null)
                node = node.l;
            return node;
        }

        public void transplant(TreeNode u, TreeNode v) {
            if (u.p == null)
                root = v;
            else if (u == u.p.l)
                u.p.l = v;
            else
                u.p.r = v;
            if (v != null)
                v.p = u.p;
        }

        public void deleteNode(TreeNode z) {
            if (z.l == null) {
                transplant(z, z.r);
            } else if (z.r == null) {
                transplant(z, z.l);
            } else {
                TreeNode y = minimum(z.r);
                if (y.p != z) {
                    transplant(y, y.r);
                    y.r = z.r;
                    if (y.r != null) y.r.p = y;
                }
                transplant(z, y);
                y.l = z.l;
                if (y.l != null) y.l.p = y;
            }
        }
    }

