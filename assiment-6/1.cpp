#include <iostream>
#include <string>
using namespace std;

#define SIZE 14
#define INFINITY_COST 99999

// -------- City Names --------
string location[SIZE] = {
    "Boston","Providence","Portland","New York",
    "Philadelphia","Baltimore","Syracuse","Buffalo",
    "Pittsburgh","Cleveland","Columbus","Detroit",
    "Indianapolis","Chicago"
};

// -------- Heuristic (Distance to Boston) --------
int heuristic[SIZE] = {
    0,50,107,215,270,360,260,400,470,550,640,610,780,860
};

// -------- Road Distance Matrix --------
int road[SIZE][SIZE];

// -------- Get Position --------
int findPosition(string name){
    for(int i=0;i<SIZE;i++)
        if(location[i]==name)
            return i;
    return -1;
}

// -------- Connect Cities --------
void connect(string A,string B,int cost){
    int i=findPosition(A);
    int j=findPosition(B);
    road[i][j]=cost;
    road[j][i]=cost;
}

// =====================================================
// GREEDY BEST FIRST SEARCH
// =====================================================
void greedySearch(int start,int target){

    cout<<"\n========== GREEDY BEST FIRST SEARCH ==========\n";

    bool closedFlag[SIZE]={false};
    int frontier[SIZE];
    int frontierCount=0;
    int stepCounter=0;

    frontier[frontierCount++]=start;

    while(frontierCount>0){

        // Select minimum heuristic
        int bestIndex=0;
        for(int i=1;i<frontierCount;i++){
            if(heuristic[frontier[i]] <
               heuristic[frontier[bestIndex]])
                bestIndex=i;
        }

        int currentNode=frontier[bestIndex];

        // Remove selected from frontier
        for(int i=bestIndex;i<frontierCount-1;i++)
            frontier[i]=frontier[i+1];
        frontierCount--;

        if(closedFlag[currentNode])
            continue;

        closedFlag[currentNode]=true;
        stepCounter++;

        cout<<"\nIteration "<<stepCounter
            <<": Processing "<<location[currentNode]
            <<" | h(n)="<<heuristic[currentNode]<<"\n";

        if(currentNode==target){
            cout<<"\nDestination Achieved.\n";
            break;
        }

        // Expand neighbours
        for(int i=0;i<SIZE;i++){
            if(road[currentNode][i]!=0 && !closedFlag[i]){
                frontier[frontierCount++]=i;
                cout<<"   -> Inserted "<<location[i]
                    <<" into frontier | h="
                    <<heuristic[i]<<"\n";
            }
        }
    }

    cout<<"\nTotal Locations Processed (Greedy): "
        <<stepCounter<<"\n";
}


// =====================================================
// A* SEARCH
// =====================================================
void aStarSearch(int start,int target){

    cout<<"\n========== A* SEARCH ==========\n";

    bool closedFlag[SIZE]={false};
    int frontier[SIZE];
    int frontierCount=0;
    int distanceFromStart[SIZE];
    int stepCounter=0;

    for(int i=0;i<SIZE;i++)
        distanceFromStart[i]=INFINITY_COST;

    distanceFromStart[start]=0;
    frontier[frontierCount++]=start;

    while(frontierCount>0){

        // Select minimum f(n)
        int bestIndex=0;
        for(int i=1;i<frontierCount;i++){
            int f1=distanceFromStart[frontier[i]]+
                   heuristic[frontier[i]];
            int f2=distanceFromStart[frontier[bestIndex]]+
                   heuristic[frontier[bestIndex]];

            if(f1<f2)
                bestIndex=i;
        }

        int currentNode=frontier[bestIndex];

        // Remove from frontier
        for(int i=bestIndex;i<frontierCount-1;i++)
            frontier[i]=frontier[i+1];
        frontierCount--;

        if(closedFlag[currentNode])
            continue;

        closedFlag[currentNode]=true;
        stepCounter++;

        cout<<"\nIteration "<<stepCounter
            <<": Processing "<<location[currentNode]
            <<" | g(n)="<<distanceFromStart[currentNode]
            <<" | h(n)="<<heuristic[currentNode]
            <<" | f(n)="
            <<distanceFromStart[currentNode]+
              heuristic[currentNode]<<"\n";

        if(currentNode==target){
            cout<<"\nDestination Achieved.\n";
            break;
        }

        // Expand neighbours
        for(int i=0;i<SIZE;i++){

            if(road[currentNode][i]!=0){

                int tentativeCost=
                    distanceFromStart[currentNode]+
                    road[currentNode][i];

                if(tentativeCost<
                   distanceFromStart[i]){

                    distanceFromStart[i]=tentativeCost;
                    frontier[frontierCount++]=i;

                    cout<<"   -> Inserted "
                        <<location[i]
                        <<" | g="
                        <<distanceFromStart[i]
                        <<" | h="
                        <<heuristic[i]
                        <<" | f="
                        <<distanceFromStart[i]+
                          heuristic[i]<<"\n";
                }
            }
        }
    }

    cout<<"\nTotal Locations Processed (A*): "
        <<stepCounter<<"\n";
}


// =====================================================
// MAIN
// =====================================================
int main(){

    cout<<"=================================================\n";
    cout<<"Time Complexity Analysis\n";
    cout<<"Greedy Best First Search  : O(V^2)\n";
    cout<<"A* Search                 : O(V^2)\n";
    cout<<"(Manual minimum selection without priority queue)\n";
    cout<<"=================================================\n";

    // Initialize matrix
    for(int i=0;i<SIZE;i++)
        for(int j=0;j<SIZE;j++)
            road[i][j]=0;

    // Build Graph
    connect("Chicago","Detroit",283);
    connect("Chicago","Indianapolis",182);
    connect("Chicago","Cleveland",345);

    connect("Detroit","Buffalo",256);
    connect("Detroit","Cleveland",169);

    connect("Indianapolis","Columbus",176);

    connect("Columbus","Cleveland",144);
    connect("Columbus","Pittsburgh",185);

    connect("Cleveland","Buffalo",189);
    connect("Cleveland","Pittsburgh",134);

    connect("Buffalo","Syracuse",150);
    connect("Buffalo","Pittsburgh",215);

    connect("Pittsburgh","Philadelphia",305);
    connect("Pittsburgh","Baltimore",247);

    connect("Baltimore","Philadelphia",101);

    connect("Philadelphia","New York",97);

    connect("New York","Boston",215);
    connect("New York","Providence",181);

    connect("Boston","Providence",50);
    connect("Boston","Portland",107);

    connect("Syracuse","Boston",312);
    connect("Syracuse","New York",254);
    connect("Syracuse","Philadelphia",253);

    int source=findPosition("Chicago");
    int destination=findPosition("Boston");

    greedySearch(source,destination);
    aStarSearch(source,destination);

    return 0;
}