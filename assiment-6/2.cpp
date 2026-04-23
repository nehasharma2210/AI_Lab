#include <iostream>
using namespace std;

#define N 5
#define INF 99999

// Maze Matrix
int maze[N][N] = {
    {2,0,0,0,1},
    {0,1,0,0,3},
    {0,3,0,1,1},
    {0,1,0,0,1},
    {3,0,0,0,3}
};

bool reached[N][N];

// Manhattan Distance Heuristic
int heuristic(int x1,int y1,int x2,int y2){
    return abs(x1-x2)+abs(y1-y2);
}

// Check valid move
bool isValid(int x,int y){
    return (x>=0 && x<N && y>=0 && y<N && maze[x][y]!=1);
}

// A* Function
void Astar(int sx,int sy,int gx,int gy){

    cout<<"\n====== Running A* ======\n";

    int gCost[N][N];
    bool closed[N][N]={false};

    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
            gCost[i][j]=INF;

    gCost[sx][sy]=0;

    while(true){

        int minF=INF;
        int cx=-1,cy=-1;

        // Select minimum f
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(!closed[i][j] && gCost[i][j]!=INF){
                    int f=gCost[i][j]+heuristic(i,j,gx,gy);
                    cout<<"Tile ("<<i<<","<<j<<") ";
                    cout<<" g="<<gCost[i][j];
                    cout<<" h="<<heuristic(i,j,gx,gy);
                    cout<<" f="<<f<<"\n";
                    if(f<minF){
                        minF=f;
                        cx=i;
                        cy=j;
                    }
                }
            }
        }

        if(cx==-1) break;

        closed[cx][cy]=true;
        reached[cx][cy]=true;

        cout<<"\nProcessing Tile ("<<cx<<","<<cy<<") ";
        cout<<" g="<<gCost[cx][cy];
        cout<<" h="<<heuristic(cx,cy,gx,gy);
        cout<<" f="<<minF<<"\n";

        if(cx==gx && cy==gy){
            cout<<"Reward Collected!\n";
            return;
        }

        int dx[4]={0,0,-1,1};
        int dy[4]={-1,1,0,0};

        for(int k=0;k<4;k++){
            int nx=cx+dx[k];
            int ny=cy+dy[k];

            if(isValid(nx,ny)){
                int newCost=gCost[cx][cy]+1;
                if(newCost<gCost[nx][ny]){
                    gCost[nx][ny]=newCost;
                }
            }
        }
    }
}

int main(){

    cout<<"=====================================\n";
    cout<<"Time Complexity: O(N^2) per goal\n";
    cout<<"Since each tile scanned repeatedly\n";
    cout<<"=====================================\n";

    int startX,startY;
    int rewards[10][2];
    int rewardCount=0;

    // Find start and rewards
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(maze[i][j]==2){
                startX=i;
                startY=j;
            }
            if(maze[i][j]==3){
                rewards[rewardCount][0]=i;
                rewards[rewardCount][1]=j;
                rewardCount++;
            }
        }
    }

    int currentX=startX;
    int currentY=startY;

    // Visit all rewards
    for(int r=0;r<rewardCount;r++){

        int gx=rewards[r][0];
        int gy=rewards[r][1];

        cout<<"\nTarget Reward at ("<<gx<<","<<gy<<")\n";

        Astar(currentX,currentY,gx,gy);

        currentX=gx;
        currentY=gy;
    }

    cout<<"\nAll Rewards Collected. Exit Maze.\n";

    cout<<"\nTiles Visited During Entire Search:\n";
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(reached[i][j])
                cout<<"("<<i<<","<<j<<") ";
        }
    }

    return 0;
}