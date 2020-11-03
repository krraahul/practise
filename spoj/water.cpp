// // #include <iostream>
// // #include <vector>
// // #include <algorithm>
// // #include <tuple>

// // using namespace std;

// // typedef std::tuple<int, int> GraphNode;
// // std::tuple <int, int> Node(int a, int b){
// //     return std::make_tuple(a, b);
// // };

// // struct compareNodes{
// //     bool operator()(std::tuple<int, int> const& n1, std::tuple<int, int> const& n2){
// //         return std::get<0>(n1) - std::get<0>(n2);
// //     }
// // };


// // void buildGraph(){
// // //   GraphNode n1 = Node(3,5);
// // //   GraphNode n2 = Node(1,4);
// // //   compareNodes a1;
// // //   std::vector<GraphNode> c1 = {n1, n2};
// // //   std::sort(c1.begin(), c1.end(), a1);
// // //   std::cout<<get<0>(c1[0])<<std::endl;
// // //   std::cout<<std::get<0>(n1);
// //     compareNodes compareFn;
// //     string testcases;
// //     getline(cin, testcases);
// //     //int testcases = stoi(testcases);
// //     for(int i=0; i< stoi(testcases); i++){
// //        string dimensions;
// //        vector<GraphNode> graphoriginal, graph;
// //        //vector<string>dimensions = getline(cin, dimensions, ' ');
// //        string RMAX = getline(cin, dimensions,' ');
       
// //        //int RMAX = int(dimensions[0]);
// //        //int CMAX = int(dimensions[1]);
       
       
// //        for(int r=0; r< RMAX; r++){
// //            string row;
// //            getline(cin, row, ' ');
// //            for(int c=0; c<CMAX;c++){
// //                int pos = r*CMAX + c;
// //                cout<<"pos = "<<pos<<endl;
// //                GraphNode n1 = Node(int(row[c]),pos);
// //                GraphNode n2 = Node(int(row[c]),pos);
// //                graphoriginal.push_back(n1);
// //                graph.push_back(n2);
// //            }
// //        }
// //        sort(graph.begin(), graph.end(), compareFn);
// //        for(int i=0;i<graph.size();i++){
// //            cout<<"hello";
// //            cout<<"graph<"<<get<0>(graph[i])<<endl;
// //        }
// //     };
    
    

// // };

// // int main(){
// //     buildGraph();
// //     return 0;
// // }

// #include <iostream>
// #include <string>
// #include <vector>
// #include <bits/stdc++.h>
// #include <tuple>
// #include <algorithm>
// #include <queue>
// #include <stack>
// #include <limits>
// using namespace std;

// template <typename T>
// vector<T> enterInputInVec(vector<T> v, string data){
//     string num;
//     stringstream ss(data);
//     while(getline(ss, num,' ' )){
//         v.push_back(stoi(num));
//     }
//     return v;
// }

// struct Tank{
//     int capacity;
//     Tank(int capacity = 0){
//         this->capacity = capacity;
//     }
// };
// // typedef std::tuple<int, int> GraphNode;
// // GraphNode Node(int a, int b){
// //     return std::make_tuple(a, b);
// // };

// // struct compareNodes{
// //     bool operator()(std::tuple<int, int> const& n1, std::tuple<int, int> const& n2){
// //         int first = std::get<0>(n1);
// //         int second = std::get<0>(n2);
// //         //cout<< "first = "<<first<<" and second = "<<second<<endl;
// //         return first < second;
// //         //return std::get<0>(n1) - std::get<0>(n2);
// //     }
// // };

// typedef struct GraphNode{
//     int value;
//     int pos;
//     bool visited;
//     GraphNode(int val, int pos,  bool visited = false){
//         this->value = val;
//         this->pos = pos;
//         this-> visited = visited;
//     }
// }Node;

// struct compareNodes{
//     bool operator()(const Node& n1, const Node& n2){
//         return n1.value < n2.value;
//     }
// };

// void printGraph(GraphNode* graph, int RMax, int CMax){
//     cout<<"-----------"<<endl;
//     int size = RMax * CMax;
//     for(int i =0; i< size; i++){
//         GraphNode node = *(graph+i);
//         cout<<node.value;
//         if( i%(CMax) == CMax-1){
//             cout<<endl;
//         }
//     }
// }

// void fillSpot(GraphNode* graph, GraphNode* original_graph, int RMax, int CMax, int index, Tank* tnk){
//     vector<int> rr = {0,0,-1,1};
//     vector<int> cc = {1,-1,0,0};
//     int min = INT_MAX;
//     GraphNode currentNode = *(graph + index);
//     int pos = currentNode.pos;
//     int x = int(pos/CMax);
//     int y = pos%CMax;
//     int current_value = currentNode.value;
//     GraphNode originalNode = *(original_graph+pos);
//     int original_value = originalNode.value;

//     for(int i =0; i<4; i++){
//         if(abs(rr[i]) == abs(cc[i])){
//             continue;
//         }
//         int neighbour_x = x + rr[i];
//         int neighbour_y = y + cc[i];
        
//         if(neighbour_x < 0 || neighbour_x >= RMax || neighbour_y < 0 || neighbour_y >=CMax){
//             continue;
//         }

        
        
//         int neighbour_pos =  (neighbour_x * CMax) + neighbour_y;
//         GraphNode neighbour_node = *(graph + neighbour_pos);
//         int neighbour_value =neighbour_node.value;
//         if(neighbour_value < current_value){
//             return;
//         }
//         if(min > neighbour_value){
//             min = neighbour_value;
//         }
        
//     };
//     Tank tank = *tnk;
//     tank.capacity = tank.capacity + (min - currentNode.value);
//     currentNode.value = min;
// }

// int exploreNeighbours(GraphNode* graph, GraphNode* original_graph, int RMax, int CMax, int index, queue<GraphNode> &q){
//     vector<int> rr = {0,0,-1,1};
//     vector<int> cc = {1,-1,0,0};
//     int min = INT_MAX;
//     GraphNode currentNode = *(graph + index);
//     int pos = currentNode.pos;
//     int x = int(pos/CMax);
//     int y = pos%CMax;
//     int current_value = currentNode.value;
//     GraphNode originalNode = *(original_graph+pos);
//     int original_value = originalNode.value;
//     //cout<<"pos = "<<pos<<endl;
//     for(int i =0; i<4; i++){
//         if(abs(rr[i]) == abs(cc[i])){
//             continue;
//         }
//         int neighbour_x = x + rr[i];
//         int neighbour_y = y + cc[i];
        
//         if(neighbour_x < 0 || neighbour_x >= RMax || neighbour_y < 0 || neighbour_y >=CMax){
//             continue;
//         }
        
        
//         int neighbour_pos =  (neighbour_x * CMax) + neighbour_y;
//         GraphNode neighbour_node = *(graph + neighbour_pos);
//         int neighbour_value =neighbour_node.value;
//         if(neighbour_value < current_value){
//             return -1;
//         }
//         if(neighbour_value == current_value && neighbour_node.visited != true){
//             q.push(neighbour_node);
//         }
//         if(min > neighbour_value){
//             min = neighbour_value;
//         }
        
//     };
//     if(min != INT_MAX){
//         cout<< "here "<<min<<endl;
//         return min;
//     }
//     cout<<"here";
//     return -1;
// }

// void fillSurface(GraphNode* graph, GraphNode* original_graph, int RMax, int CMax, int index, Tank &tank){
//     GraphNode currentNode = *(graph + index);
//     int surfaceHeight = currentNode.value;
//     stack<GraphNode> st;
//     queue<GraphNode> que;
//     que.push(currentNode);
//     int min = INT_MAX;
//     bool abrupt_break = false;
//     while(!que.empty()){
//         GraphNode curr_node = que.front();
//         que.pop();
//         curr_node.visited = true;
//         st.push(curr_node);
//         int index = curr_node.pos;
//         int newmin = exploreNeighbours(graph, original_graph,  RMax, CMax, index, que);
//         if(newmin == -1){
//             abrupt_break = true;
//             break;
//         }
//         if(newmin < min){
//             min = newmin;
//         }
//     }
    
//     while(!st.empty()){
//         GraphNode gnode = st.top();
//         st.pop();
//         gnode.visited = false;
//         if(!abrupt_break){
//            tank.capacity = tank.capacity + (min - gnode.value); 
//         }
        
//     }
    
// }


// void buildGraph(){
//     string row;
//     getline(cin, row);
//     int testcases = stoi(row);
//     cout<<"Testcases = "<<testcases<<endl;
//     for(int i=0; i<testcases; i++){
//         vector<GraphNode>graphoriginal,graph;
//         Tank tank = Tank(0);
//         string dimrow;
//         vector<int> dimvec;
//         getline(cin, dimrow);
//         dimvec = enterInputInVec(dimvec, dimrow);
//         int RMax = dimvec[0];
//         int CMax = dimvec[1];
        
//         for(int r = 0; r<RMax; r++){
//             vector<int> rvec;
//             string row;
//             getline(cin, row);
//             //cout<<"CMAX = "<<CMax<<endl;
//             rvec = enterInputInVec(rvec, row);
//             //cout<<"rvec size = "<<rvec.size()<<endl;
//             for(int c=0; c<CMax; c++){
//                 int pos = r*CMax + c;
//                 //cout<<"here pos = "<<pos<<endl;
//                 GraphNode norg = Node(rvec[c], pos);
//                 GraphNode n = Node(rvec[c], pos);
//                 graph.push_back(n);
//                 graphoriginal.push_back(norg);
//                 //cout<<rvec[c]<<" @pos = "<<pos;
//             }
//             cout<<endl;
//         }
//         compareNodes compareFn;
//         // sort(graph.begin(), graph.end(), [](GraphNode const& n1, GraphNode const& n2){
//         //     return get<0>(n1) - get<0>(n2);
//         // });
//         sort(graph.begin(), graph.end(), compareFn);
//         fillSpot(graph.data(), graphoriginal.data(), RMax, CMax, 10, &tank); //passing reference to function
//         // for(int p = 0; p < graph.size(); p++){
//         //     int pos = graph[p].pos;
//         //     cout<<"for pos = "<<pos<<endl;
//         //     fillSpot(graph.data(), graphoriginal.data(), RMax, CMax, pos, &tank); //passing reference to function
//         //     fillSurface(graph.data(), graphoriginal.data(), RMax, CMax, pos, tank);
//         //     if(pos == 10){
//         //         printGraph(graph.data(), RMax, CMax);
//         //     }
//         //     cout<<"tank = "<<tank.capacity<<endl;
//         // }
//         cout<<" Tank capacity = "<<tank.capacity<<endl;
//         printGraph(graph.data(), RMax, CMax);
//         //cout<<graph[0].value;
//         // for(int k=0; k<graph.size();k++){
//         //     cout<<get<0>(graph[k])<<endl;
//         // }
//         // for(int k=0; k<graph.size(); k++){
//         //     cout<< graph[k].value;
//         // }
        
        
        
        
//     }
// }



// int main() {
    
//     //  vector<GraphNode> graph;
//     //  GraphNode n1 = Node(2,4);
//     //  //graph.push_back(n1);
//     //  GraphNode n2 = Node(3,4);
//     //  //graph.push_back(n2);
//     //  GraphNode n3 = Node(1,4);
//     //  //graph.push_back(n3);
//     //  GraphNode n4 = Node(7,4);
//     //  //graph.push_back(n4);
//     //  GraphNode n5 = Node(0,4);
//     //  //graph.push_back(n5);
//     //  graph = {n1,n2,n3,n4,n5};
//     //     sort(graph.begin(), graph.end(), [](const GraphNode& n1, const GraphNode& n2){
//     //         int first = std::get<0>(n1);
//     //         int second = std::get<0>(n2);
//     //         cout<< "first = "<<first<<" and second = "<<second<<endl;
//     //         cout<< "first - second: "<<first- second<<endl;
//     //         return first < second;
//     //     });
//     //     for(int k=0; k<graph.size();k++){
//     //         cout<<get<0>(graph[k])<<endl;
//     //     }
     
//     buildGraph();
//     return 0;
// }





#include <iostream>
#include<queue>
#include<stack>
#include<string>
#include<climits>
#include<algorithm>
#include<sstream>

using namespace std;


void convertStringToVector(vector<int>& v, string& data, char delim =  ' '){
    stringstream ss(data);
    string numstr;
    while(getline(ss, numstr, delim )){
        v.push_back(stoi(numstr));
    }
}

typedef struct Node{
    int value;
    bool visited;
    int pos;
    Node(int val, int pos, bool isvisited = false){
        this->value = val;
        
        this->pos = pos;
        this->visited = isvisited;
    }
}Node;



typedef struct Tank{
    int level;
    Tank(int capacity = 0){
        this->level = capacity;
    }
}Tank;

void fillSpot(int index,int level, vector<Node>& graph, vector<Node>& ograph, Tank& tank, int rmax, int cmax){
    int pos = graph[index].pos;
    vector<int> rr = {1,-1,0,0};
    vector<int> cc = {0,0,1,-1};
    Node& currentNode = ograph[pos];
    int x = int(pos / cmax);
    int y = pos % cmax;
    int min = INT_MAX;
    int currentLevel = currentNode.value;
    for(int i = 0; i< rr.size(); i++){
        int newx = x + rr[i];
        int newy = y + cc[i];
        
        int newpos = (newx * cmax) + newy;
        if(newx <0 || newy < 0 || newx >=rmax || newy>=cmax){
            return;
        }
        
        int neighbour_level = ograph[newpos].value;
        if(neighbour_level < level || neighbour_level == currentLevel){
            return;
        }
        
        if(neighbour_level > level && neighbour_level < min){
            min = neighbour_level;
        }
        
    }
    if(min < INT_MAX && min > currentLevel ){
        
        tank.level = tank.level + (min - currentNode.value);
        currentNode.value = min;  
    }
};

int explore_neighbours(int currNodePos, vector<Node>& graph, vector<Node>& ograph, Tank& tank, int rmax, int cmax, queue<int>& que, int surfaceHeight){
    Node& currNode = ograph[currNodePos];
    int level = currNode.value;
    int pos = currNode.pos;
    vector<int> rr = {1,-1,0,0};
    vector<int> cc = {0,0,1,-1};
   
    int x = int(pos / cmax);
    int y = pos % cmax;
    int min = INT_MAX;
    for(int i = 0; i< rr.size(); i++){
        int newx = x + rr[i];
        int newy = y + cc[i];
        
        int newpos = (newx * cmax) + newy;
        if(newx <0 || newy < 0 || newx >=rmax || newy>=cmax){
            return -1;
        }
        
        Node& neighbourNode = ograph[newpos];
        int neighbour_level = ograph[newpos].value;
  
      
        if(neighbour_level < surfaceHeight){
            return -1;
        }
       
        if(neighbour_level == level && !neighbourNode.visited){
            neighbourNode.visited = true;
            que.push(neighbourNode.pos);
            
        }
        if(neighbour_level > surfaceHeight && neighbour_level < min && !neighbourNode.visited){
            min = neighbour_level;
        }
        
    }
    return min;
    
};

void fillSurface(int index, vector<Node>& graph, vector<Node>& ograph, Tank& tank, int rmax, int cmax){
    int pos = graph[index].pos;
    queue<int> que;
    stack<int> stk;
  
    const int LOWER_HEIGHT_FOUND = -1;
    int minSurfaceLevel = INT_MAX;
    bool abrupt_break = false;
    
    Node& currentNode = ograph[pos];
    que.push(currentNode.pos);
 
    int currentLevel = currentNode.value;
    while(!que.empty()){
        int currNodePos = que.front();
        que.pop();
        Node& currNode = ograph[currNodePos];
        stk.push(currNodePos);
        currNode.visited = true;
        int newMinSurfaceLevel = explore_neighbours(currNodePos, graph, ograph, tank, rmax, cmax, que, currentLevel);
        if(newMinSurfaceLevel == LOWER_HEIGHT_FOUND){
            abrupt_break = true;
            break;
        }
        
        if(newMinSurfaceLevel > currentLevel && newMinSurfaceLevel < minSurfaceLevel){
            minSurfaceLevel = newMinSurfaceLevel;
        }
    }
    if(abrupt_break){
        while(!que.empty()){
            Node & n = ograph[que.front()];
            que.pop();
            n.visited = false;
        }
    }
    while(!stk.empty()){
        int nodePos = stk.top();
        stk.pop();
        Node& n = ograph[nodePos];
        if(abrupt_break){
            n.visited = false;
        }else if(minSurfaceLevel < INT_MAX){
            tank.level = tank.level + (minSurfaceLevel - currentLevel);
            n.value = minSurfaceLevel;
            
        }
        n.visited = false;
    }
}

void buildGraph(){
    string testcases;
    getline(cin, testcases);
    int testcase = 0;
    while(testcase < stoi(testcases)){
        vector<Node> graph, ograph;
        Tank tank = Tank();
        string dims;
        getline(cin, dims);
        vector<int> dimensions;
        convertStringToVector(dimensions, dims);
        
        int rmax = dimensions[0];
        int cmax = dimensions[1];
        
        for (int i =0 ; i < rmax; i++){
            string row;
            getline(cin, row);
            vector<int> rowdata;
            convertStringToVector(rowdata, row, ' ');
            for(int j= 0; j < cmax; j++){
                int pos = i * cmax + j;
                int val = rowdata[j];
                Node gn = Node(val, pos, false);
                Node ogn = Node(val, pos, false);
                graph.push_back(gn);
                ograph.push_back(ogn);
            }
        }
        
        //sort the graph based on value
        sort(graph.begin(), graph.end(), [](Node const& n1, Node const& n2)->bool{
            return n1.value < n2.value;
        });
        

        for(int i = 0; i < graph.size(); i++){
            Node leastfilledNode = graph[i];
            int position = leastfilledNode.pos;
            int level = leastfilledNode.value;
            fillSpot(i, level, graph, ograph, tank,  rmax, cmax);
            fillSurface(i, graph, ograph, tank,  rmax, cmax);
        }

        cout<<tank.level<<endl;
        
        testcase++;
    }
}

int main() {
    buildGraph();
    return 0;
}