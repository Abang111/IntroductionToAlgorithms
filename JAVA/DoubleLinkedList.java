
    public class DoubleLinkedList {
        public DoubleLinkedList(Node nil) {
            this.nil = nil;
        }

        static class Node {
            String key;
            Node prev;
            Node next;

            Node(String key) {
                this.key = key;
                this.prev = this.next = null;
            }
        }

        private Node nil; // Sentinel node

        public void DoublyCircularLinkedList() {
            nil = new Node("NIL");
            nil.next = nil;
            nil.prev = nil;
        }

        public void listInsert(Node node) {
            // Insert at the head (right after NIL)
            node.next = nil.next;
            nil.next.prev = node;
            nil.next = node;
            node.prev = nil;
        }

        public Node listSearch(String key) {
            Node x = nil.next;
            while (x != nil && !x.key.equals(key)) {
                x = x.next;
            }
            return x;
        }

        public void listDelete(Node node) {
            if (node == nil) {
                System.out.println("Attempted to delete NIL node; skipping.");
                return;
            }
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }

        public String display() {
            StringBuilder sb = new StringBuilder();
            Node x = nil.next;
            while (x != nil) {
                sb.append(x.key).append(" ");
                x = x.next;
            }
            return sb.toString().trim();
        }
    }


