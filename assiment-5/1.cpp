#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct State {
    int girls_left;
    int boys_left;
    int boat; // 0 = Left, 1 = Right

    // Required for set<State>
    bool operator<(const State& other) const {
        if (girls_left != other.girls_left)
            return girls_left < other.girls_left;
        if (boys_left != other.boys_left)
            return boys_left < other.boys_left;
        return boat < other.boat;
    }
};

int explored = 0;

// Check if state is valid
bool isValid(State s) {
    int girls_right = 3 - s.girls_left;
    int boys_right = 3 - s.boys_left;

    // Left side condition
    if (s.girls_left > 0 && s.boys_left > s.girls_left)
        return false;

    // Right side condition
    if (girls_right > 0 && boys_right > girls_right)
        return false;

    return true;
}

// Goal test
bool isGoal(State s) {
    return (s.girls_left == 0 && s.boys_left == 0 && s.boat == 1);
}

// Print state
void printState(State s) {
    cout << "(G_L=" << s.girls_left
         << ", B_L=" << s.boys_left
         << ", Boat=" << (s.boat == 0 ? "Left" : "Right")
         << ")" << endl;
}

// Generate next states
vector<State> getNextStates(State s) {
    vector<State> nextStates;
    int direction = (s.boat == 0) ? -1 : 1;

    vector<pair<int,int>> moves = {
        {1,0}, {2,0}, {0,1}, {0,2}, {1,1}
    };

    for (auto move : moves) {
        State newState;
        newState.girls_left = s.girls_left + direction * move.first;
        newState.boys_left  = s.boys_left  + direction * move.second;
        newState.boat = 1 - s.boat;

        if (newState.girls_left >= 0 && newState.girls_left <= 3 &&
            newState.boys_left >= 0 && newState.boys_left <= 3 &&
            isValid(newState)) {
            nextStates.push_back(newState);
        }
    }

    return nextStates;
}

// Depth Limited Search
bool DLS(State current, int limit, set<State>& reached, vector<State>& path) {
    explored++;
    path.push_back(current);
    reached.insert(current);

    if (isGoal(current))
        return true;

    if (limit == 0) {
        path.pop_back();
        return false;
    }

    for (State next : getNextStates(current)) {
        if (reached.find(next) == reached.end()) {
            if (DLS(next, limit - 1, reached, path))
                return true;
        }
    }

    path.pop_back();
    return false;
}

// Iterative Deepening Search
bool IDS(State start) {
    for (int depth = 0; depth <= 20; depth++) {
        cout << "\n===== Depth = " << depth << " =====\n";

        set<State> reached;
        vector<State> path;
        explored = 0;

        if (DLS(start, depth, reached, path)) {
            cout << "\nGoal Found at Depth " << depth << "\n\nSolution Path:\n";
            for (State s : path)
                printState(s);

            cout << "\nTotal Explored States: " << explored << endl;
            return true;
        }

        cout << "Explored States at Depth " << depth << ": "
             << explored << endl;
    }

    return false;
}

int main() {
    State start = {3, 3, 0};
    cout<<"Time Complexity:O(b^L)"<<endl;
    cout << "============================="<<endl;
    cout << "Depth Limited Search (limit=3)"<<endl;
    cout << "============================="<<endl;

    set<State> reached;
    vector<State> path;
    explored = 0;

    if (DLS(start, 3, reached, path)) {
        cout << "\nSolution Found:\n";
        for (State s : path)
            printState(s);
    } else {
        cout << "\nNo solution found within depth 3.\n";
    }

    cout << "Total Explored States: " << explored << endl;

    cout << "\n\n=============================\n";
    cout << "Iterative Deepening Search\n";
    cout<<"Time Complexity:O(b^d)"<<endl;
    cout << "=============================\n";

    IDS(start);

    return 0;
}