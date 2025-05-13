#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Vertex {
    string key;
    vector<pair<Vertex*, int>> adjacent;
    Vertex* prev = nullptr;

    Vertex(string k) : key(k) {}
};

class Graph {
public:
    unordered_map<string, Vertex*> nodes;

    void addVertex(const string& key) {
        if (nodes.find(key) == nodes.end()) {
            nodes[key] = new Vertex(key);
        }
    }

    bool addEdge(const string& u, const string& v, int weight) {
        if (nodes.find(u) == nodes.end() || nodes.find(v) == nodes.end())
            throw invalid_argument("Both vertices must exist.");
        for (auto& [neighbor, _] : nodes[u]->adjacent) {
            if (neighbor->key == v)
                return false; // Edge already exists
        }
        nodes[u]->adjacent.push_back({nodes[v], weight});
        return true;
    }

    pair<Vertex*, int>* contains(vector<pair<Vertex*, int>>& lst, Vertex* vertex) {
        for (auto& p : lst) {
            if (p.first == vertex)
                return &p;
        }
        return nullptr;
    }

    vector<Vertex*> dijkstra(const string& start_key, const string& end_key) {
        vector<pair<Vertex*, int>> open_list = {{nodes[start_key], 0}};
        vector<pair<Vertex*, int>> closed_list;

        _recursion(open_list, closed_list, nodes[end_key]);

        vector<Vertex*> path;
        Vertex* node = nodes[end_key];
        while (node) {
            path.push_back(node);
            node = node->prev;
        }
        reverse(path.begin(), path.end());
        return path;
    }

private:
    void _recursion(vector<pair<Vertex*, int>>& open_list, vector<pair<Vertex*, int>>& closed_list, Vertex* end_node) {
        if (contains(closed_list, end_node) || open_list.empty())
            return;

        auto current = open_list.front();
        open_list.erase(open_list.begin());
        closed_list.push_back(current);

        Vertex* u = current.first;
        int u_dist = current.second;

        for (auto& [neighbor, weight] : u->adjacent) {
            if (contains(closed_list, neighbor)) continue;

            auto existing = contains(open_list, neighbor);
            int new_dist = u_dist + weight;

            if (existing) {
                if (new_dist < existing->second) {
                    open_list.erase(remove(open_list.begin(), open_list.end(), *existing), open_list.end());
                } else {
                    continue;
                }
            }

            neighbor->prev = u;
            open_list.push_back({neighbor, new_dist});
        }

        sort(open_list.begin(), open_list.end(), [](auto& a, auto& b) {
            return a.second < b.second;
        });

        _recursion(open_list, closed_list, end_node);
    }
};
