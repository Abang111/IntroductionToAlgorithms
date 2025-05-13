import java.util.*;

class Node {
    String key;
    List<Neighbor> adjacent;

    Node(String key) {
        this.key = key;
        this.adjacent = new ArrayList<>();
    }

    static class Neighbor {
        Node node;
        int weight;

        Neighbor(Node node, int weight) {
            this.node = node;
            this.weight = weight;
        }
    }
}

public class Graph {
    Map<String, Node> nodes = new HashMap<>();
    List<Node> openList;
    List<Node> closedList;
    Set<String> visited;

    public void addNode(String key, List<String> neighbors, List<Integer> weights) {
        Node node = new Node(key);
        nodes.put(key, node);

        if (neighbors != null) {
            if (weights == null) {
                weights = new ArrayList<>(Collections.nCopies(neighbors.size(), 1));
            }

            for (int i = 0; i < neighbors.size(); i++) {
                String neighborKey = neighbors.get(i);
                int weight = weights.get(i);
                if (nodes.containsKey(neighborKey)) {
                    node.adjacent.add(new Node.Neighbor(nodes.get(neighborKey), weight));
                }
            }
        }
    }

    public void addEdge(String u, String v, int weight) {
        Node uNode = nodes.get(u);
        Node vNode = nodes.get(v);
        boolean exists = false;
        for (Node.Neighbor neighbor : uNode.adjacent) {
            if (neighbor.node.key.equals(v)) {
                exists = true;
                break;
            }
        }
        if (!exists) {
            uNode.adjacent.add(new Node.Neighbor(vNode, weight));
        }
    }

    public List<Node> bdfs(String startKey, String mode) {
        if (!nodes.containsKey(startKey)) return new ArrayList<>();

        openList = new LinkedList<>();
        closedList = new ArrayList<>();
        visited = new HashSet<>();

        openList.add(nodes.get(startKey));
        _recurse(mode.toUpperCase());

        return closedList;
    }

    private void _recurse(String mode) {
        if (openList.isEmpty()) return;

        Node current = openList.remove(0);
        closedList.add(current);
        visited.add(current.key);

        for (Node.Neighbor neighbor : current.adjacent) {
            if (!visited.contains(neighbor.node.key) && !openList.contains(neighbor.node)) {
                if (mode.equals("BFS")) {
                    openList.add(neighbor.node);
                } else if (mode.equals("DFS")) {
                    openList.add(0, neighbor.node);
                }
            }
        }

        _recurse(mode);
    }

    // Optional: Display traversal keys
    public static List<String> extractKeys(List<Node> nodeList) {
        List<String> keys = new ArrayList<>();
        for (Node n : nodeList) {
            keys.add(n.key);
        }
        return keys;
    }

    // === 示例测试 ===
    public static void main(String[] args) {
        Graph graph = new Graph();

        // Add nodes
        graph.addNode("A", null, null);
        graph.addNode("B", null, null);
        graph.addNode("C", null, null);
        graph.addNode("D", null, null);
        graph.addNode("E", null, null);

        // Add edges
        graph.addEdge("A", "B", 1);
        graph.addEdge("A", "C", 1);
        graph.addEdge("B", "D", 1);
        graph.addEdge("C", "E", 1);

        // BFS traversal
        List<Node> bfsResult = graph.bdfs("A", "BFS");
        System.out.println("BFS: " + extractKeys(bfsResult));

        // DFS traversal
        List<Node> dfsResult = graph.bdfs("A", "DFS");
        System.out.println("DFS: " + extractKeys(dfsResult));
    }
}


