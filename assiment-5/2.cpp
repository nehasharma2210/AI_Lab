#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct State {
    int girls_left;
    int boys_left;
    int boat; // 0 = Left, 1 = Right

    // For set comparison
    bool operator<(const State& other) const {
        if (girls_left != other.girls_left)
            return girls_left < other.girls_left;
        if (boys_left != other.boys_left)
            return boys_left < other.boys_left;
        return boat < other.boat;
    }
};

int explored = 0;

// Check if state valid
bool isValid(State s) {
    int girls_right = 3 - s.girls_left;
    int boys_right = 3 - s.boys_left;

    // Left side check
    if (s.girls_left > 0 && s.boys_left > s.girls_left)
        return false;

    // Right side check
    if (girls_right > 0 && boys_right > girls_right)
        return false;

    return true;
}

// Goal check
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

// Generate next states manually
vector<State> getNextStates(State s) {

    vector<State> nextStates;
    int direction;

    if (s.boat == 0)
        direction = -1;  // boat moving Left -> Right
    else
        direction = 1;   // boat moving Right -> Left

    // All possible moves (1 or 2 persons)
    int move[5][2] = {
        {1,0},
        {2,0},
        {0,1},
        {0,2},
        {1,1}
    };

    for (int i = 0; i < 5; i++) {
        State newState;

        newState.girls_left = s.girls_left + direction * move[i][0];
        newState.boys_left  = s.boys_left  + direction * move[i][1];
        newState.boat = 1 - s.boat;

        if (newState.girls_left >= 0 && newState.girls_left <= 3 &&
            newState.boys_left >= 0 && newState.boys_left <= 3 &&
            isValid(newState)) {
            nextStates.push_back(newState);
        }
    }

    return nextStates;
}

// Depth Limited Search used inside IDS
bool DLS(State current, int limit, set<State>&  reached, vector<State>& path) {

    explored++;
    path.push_back(current);
     reached.insert(current);

    if (isGoal(current))
        return true;

    if (limit == 0) {
        path.pop_back();
        return false;
    }

    vector<State> nextStates = getNextStates(current);

    for (int i = 0; i < nextStates.size(); i++) {
        if ( reached.find(nextStates[i]) ==  reached.end()) {
            if (DLS(nextStates[i], limit - 1,  reached, path))
                return true;
        }
    }

    path.pop_back();
    return false;
}

// Iterative Deepening Search
void IDS(State start) {

    for (int depth = 0; depth <= 20; depth++) {

        cout << "\n=============================\n";
        cout << "Trying Depth = " << depth << endl;
        cout << "=============================\n";

        set<State>  reached;
        vector<State> path;
        explored = 0;

        if (DLS(start, depth,  reached, path)) {

            cout << "\nGoal Found at Depth = " << depth << endl;
            cout << "\nSolution Path:\n";

            for (int i = 0; i < path.size(); i++)
                printState(path[i]);

            cout << "\nTotal Explored States = " << explored << endl;
            return;
        }

        cout << "Explored States at Depth " << depth
             << " = " << explored << endl;
    }
}

int main() {
    cout<<"Time Complexity:O(b^d)"<<endl;
    State start;
    start.girls_left = 3;
    start.boys_left = 3;
    start.boat = 0;

    IDS(start);

    return 0;
}