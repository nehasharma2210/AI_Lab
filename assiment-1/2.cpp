#include <bits/stdc++.h>
using namespace std;

map<string, vector<string>> graph = {
    {"Raj", {"Priya", "Sunil"}},
    {"Priya", {"Raj", "Aarav", "Neha"}},
    {"Aarav", {"Priya", "Neha", "Arjun"}},
    {"Sunil", {"Raj", "Akash", "Sneha"}},
    {"Akash", {"Sunil", "Neha"}},
    {"Neha", {"Priya", "Akash", "Rahul"}},
    {"Sneha", {"Sunil", "Rahul", "Maya"}},
    {"Rahul", {"Neha", "Sneha", "Pooja"}},
    {"Maya", {"Sneha"}},
    {"Arjun", {"Aarav", "Pooja"}},
    {"Pooja", {"Rahul", "Arjun"}}
};

/* -------- BFS -------- */
void BFS(string start)
{
    set<string> visited;
    queue<string> q;

    q.push(start);
    visited.insert(start);

    cout << "BFS Tree: ";

    while (!q.empty())
    {
        string node = q.front();
        q.pop();
        cout << node << " ";

        for (auto &neighbor : graph[node])
        {
            if (!visited.count(neighbor))
            {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
    cout << endl;
}

/* -------- DFS -------- */
void DFS(string node, set<string> &visited)
{
    visited.insert(node);
    cout << node << " ";

    for (auto &neighbor : graph[node])
    {
        if (!visited.count(neighbor))
            DFS(neighbor, visited);
    }
}

int main()
{
    cout << "Social Media Network Traversal\n";

    BFS("Raj");

    cout << "DFS Tree: ";
    set<string> visited;
    DFS("Raj", visited);

    return 0;
}
