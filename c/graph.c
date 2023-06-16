#include <stdio.h>
#include <stdlib.h>

// Structure for a node in the adjacency list
struct Node {
    int vertex;
    struct Node* next;
};

// Structure for the graph
struct Graph {
    int numVertices;
    struct Node** adjacencyList;
};

// Function to create a new node
struct Node* createNode(int vertex) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->vertex = vertex;
    newNode->next = NULL;
    return newNode;
}

// Function to create a graph with given number of vertices
struct Graph* createGraph(int numVertices) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = numVertices;
    
    graph->adjacencyList = (struct Node**)malloc(numVertices * sizeof(struct Node*));
    
    int i;
    for (i = 0; i < numVertices; i++) {
        graph->adjacencyList[i] = NULL;
    }
    
    return graph;
}

// Function to add an edge to the graph
void addEdge(struct Graph* graph, int src, int dest) {
    // Add an edge from source to destination
    struct Node* newNode = createNode(dest);
    newNode->next = graph->adjacencyList[src];
    graph->adjacencyList[src] = newNode;
    
    // Add an edge from destination to source (assuming undirected graph)
    newNode = createNode(src);
    newNode->next = graph->adjacencyList[dest];
    graph->adjacencyList[dest] = newNode;
}

// Function to print the graph
void printGraph(struct Graph* graph) {
    int i;
    for (i = 0; i < graph->numVertices; i++) {
        struct Node* currentNode = graph->adjacencyList[i];
        printf("Adjacency list of vertex %d: ", i);
        while (currentNode) {
            printf("%d -> ", currentNode->vertex);
            currentNode = currentNode->next;
        }
        printf("NULL\n");
    }
}

int main() {
    int numVertices = 5;
    struct Graph* graph = createGraph(numVertices);
    
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);
    
    printGraph(graph);
    
    return 0;
}
