#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <string>
#include <algorithm>

class Vertex {
public:
    std::string key;

    struct Neighbor {
        Vertex* vertex;
        int weight;
        Neighbor(Vertex* v, int w) : vertex(v), weight(w) {}
    };

    std::vector<Neighbor> adjacent;

    Vertex(const std::string& k) : key(k) {}
};

class Graph {
public:
    std::unordered_map<std::string, Vertex*> nodes;
    std::deque<Vertex*> openList;
    std::vector<Vertex*> closedList;
    std::unordered_set<std::string> visited;

    ~Graph() {
        for (auto& pair : nodes) {
            delete pair.second;
        }
    }

    void addVertex(const std::string& key,
                   const std::vector<std::string>* neighbors = nullptr,
                   const std::vector<int>* weights = nullptr) {
        Vertex* vertex = new Vertex(key);
        nodes[key] = vertex;

        if (neighbors) {
            std::vector<int> localWeights;
            if (!weights) {
                localWeights.assign(neighbors->size(), 1);
                weights = &localWeights;
            }

            for (size_t i = 0; i < neighbors->size(); ++i) {
                const std::string& neighborKey = (*neighbors)[i];
                int weight = (*weights)[i];
                if (nodes.count(neighborKey)) {
                    vertex->adjacent.emplace_back(nodes[neighborKey], weight);
                }
            }
        }
    }

    void addEdge(const std::string& u, const std::string& v, int weight) {
        Vertex* uNode = nodes[u];
        Vertex* vNode = nodes[v];
        bool exists = false;
        for (const auto& neighbor : uNode->adjacent) {
            if (neighbor.vertex->key == v) {
                exists = true;
                break;
            }
        }
        if (!exists) {
            uNode->adjacent.emplace_back(vNode, weight);
        }
    }

    std::vector<Vertex*> bdfs(const std::string& startKey, const std::string& mode) {
        if (!nodes.count(startKey)) return {};

        openList.clear();
        closedList.clear();
        visited.clear();

        openList.push_back(nodes[startKey]);
        _recurse(mode == "DFS" ? "DFS" : "BFS");

        return closedList;
    }

    void _recurse(const std::string& mode) {
        if (openList.empty()) return;

        Vertex* current = openList.front();
        openList.pop_front();
        closedList.push_back(current);
        visited.insert(current->key);

        for (auto& neighbor : current->adjacent) {
            if (!visited.count(neighbor.vertex->key) &&
                std::find(openList.begin(), openList.end(), neighbor.vertex) == openList.end()) {

                if (mode == "BFS") {
                    openList.push_back(neighbor.vertex);
                } else if (mode == "DFS") {
                    openList.push_front(neighbor.vertex);
                }
            }
        }

        _recurse(mode);
    }

    static std::vector<std::string> extractKeys(const std::vector<Vertex*>& vertexList) {
        std::vector<std::string> keys;
        for (const auto* v : vertexList) {
            keys.push_back(v->key);
        }
        return keys;
    }
};

// === 示例测试 ===
int main() {
    Graph graph;

    // 添加顶点
    graph.addVertex("A");
    graph.addVertex("B");
    graph.addVertex("C");
    graph.addVertex("D");
    graph.addVertex("E");

    // 添加边
    graph.addEdge("A", "B", 1);
    graph.addEdge("A", "C", 1);
    graph.addEdge("B", "D", 1);
    graph.addEdge("C", "E", 1);

    // BFS 遍历
    auto bfsResult = graph.bdfs("A", "BFS");
    auto bfsKeys = Graph::extractKeys(bfsResult);
    std::cout << "BFS: ";
    for (const auto& k : bfsKeys) std::cout << k << " ";
    std::cout << "\n";

    // DFS 遍历
    auto dfsResult = graph.bdfs("A", "DFS");
    auto dfsKeys = Graph::extractKeys(dfsResult);
    std::cout << "DFS: ";
    for (const auto& k : dfsKeys) std::cout << k << " ";
    std::cout << "\n";

    return 0;
}
