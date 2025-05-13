
    import java.util.*;

    class Vertex {
        String key;
        List<Edge> adjacent = new ArrayList<>();
        Vertex prev = null;

        Vertex(String key) {
            this.key = key;
        }

        static class Edge {
            Vertex neighbor;
            int weight;

            Edge(Vertex neighbor, int weight) {
                this.neighbor = neighbor;
                this.weight = weight;
            }
        }
    }

    public class Dijkstra {
        Map<String, Vertex> nodes = new HashMap<>();

        public void addVertex(String key) {
            nodes.putIfAbsent(key, new Vertex(key));
        }

        public boolean addEdge(String u, String v, int weight) {
            if (!nodes.containsKey(u) || !nodes.containsKey(v))
                throw new IllegalArgumentException("Both vertices must exist.");
            for (Vertex.Edge e : nodes.get(u).adjacent) {
                if (e.neighbor.key.equals(v)) return false;
            }
            nodes.get(u).adjacent.add(new Vertex.Edge(nodes.get(v), weight));
            return true;
        }

        private Vertex.Edge contains(List<Map.Entry<Vertex, Integer>> lst, Vertex v) {
            for (Map.Entry<Vertex, Integer> entry : lst) {
                if (entry.getKey() == v)
                    return new Vertex.Edge(entry.getKey(), entry.getValue());
            }
            return null;
        }

        public List<Vertex> dijkstra(String startKey, String endKey) {
            List<Map.Entry<Vertex, Integer>> openList = new ArrayList<>();
            List<Map.Entry<Vertex, Integer>> closedList = new ArrayList<>();

            openList.add(new AbstractMap.SimpleEntry<>(nodes.get(startKey), 0));
            _recursion(openList, closedList, nodes.get(endKey));

            List<Vertex> path = new ArrayList<>();
            Vertex node = nodes.get(endKey);
            while (node != null) {
                path.add(node);
                node = node.prev;
            }
            Collections.reverse(path);
            return path;
        }

        private void _recursion(List<Map.Entry<Vertex, Integer>> openList,
                                List<Map.Entry<Vertex, Integer>> closedList,
                                Vertex endNode) {
            if (contains(closedList, endNode) != null || openList.isEmpty())
                return;

            Map.Entry<Vertex, Integer> current = openList.remove(0);
            closedList.add(current);

            Vertex u = current.getKey();
            int uDist = current.getValue();

            for (Vertex.Edge e : u.adjacent) {
                Vertex neighbor = e.neighbor;
                int weight = e.weight;

                if (contains(closedList, neighbor) != null) continue;

                Vertex.Edge existing = contains(openList, neighbor);
                int newDist = uDist + weight;

                if (existing != null) {
                    if (newDist >= existing.weight) continue;
                    openList.removeIf(entry -> entry.getKey() == neighbor);
                }

                neighbor.prev = u;
                openList.add(new AbstractMap.SimpleEntry<>(neighbor, newDist));
            }

            openList.sort(Comparator.comparingInt(Map.Entry::getValue));
            _recursion(openList, closedList, endNode);
        }
    }


