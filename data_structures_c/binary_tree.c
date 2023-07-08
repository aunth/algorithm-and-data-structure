#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node
{
    int value;
    struct node *left;
    struct node *right;
} node;

typedef struct BinaryTree
{
    node *root;
} BinaryTree;

void insert(BinaryTree *tree, int value)
{
    node *new_node = (node *)malloc(sizeof(node));
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->value = value;
    node *current_node = tree->root;
    if (current_node == NULL)
    {
        tree->root = new_node;
        return;
    }
    while (current_node != NULL)
    {
        if (current_node->value > value)
        {
            if (current_node->left == NULL)
            {
                current_node->left = new_node;
                return;
            }
            current_node = current_node->left;
        }
        else
        {
            if (current_node->right == NULL)
            {
                current_node->right = new_node;
                return;
            }
            current_node = current_node->right;
        }
    }
}

bool lookup(BinaryTree *tree, int value)
{
    node *current_node = tree->root;
    while (current_node != NULL)
    {
        if (current_node->value > value)
            current_node = current_node->left;
        else if (current_node->value < value)
            current_node = current_node->right;
        else
            return true;
    }
    return false;
}

node *delete_node(node *Node, int value)
{
    if (Node == NULL)
        return NULL;
    if (Node->value == value)
    {
        if (Node->left == NULL && Node->right == NULL)
            return NULL;
        if (Node->left == NULL)
            return Node->right;
        if (Node->right == NULL)
            return Node->left;
        node *tmp = Node->right;
        while (tmp->left)
            tmp = tmp->left;
        Node->value = tmp->value;
        Node->right = delete_node(Node->right, tmp->value);
        tmp->left = Node->left;
return Node->right;
    }
    else if (Node->value > value)
        Node->left = delete_node(Node->left, value);
    else
        Node->right = delete_node(Node->right, value);
    return Node;
}

void delete(BinaryTree *tree, int value)
{
    tree->root = delete_node(tree->root, value);
}

void printTreeHelper(node *node, int space) {
    if (node == NULL)
        return;
    int i;
    printTreeHelper(node->right, space+5);
    printf("\n");
    for (i = 0; i < space; i++) {
        printf(" ");
    }
    printf("%d\n", node->value);
    printTreeHelper(node->left, space+5);
}

void printTree(node *root) {
    printTreeHelper(root, 0);
}

int main(void)
{
    node *root = (node *)malloc(sizeof(node));
    root->value = 15;
    root->left = NULL;
    root->right = NULL;
    BinaryTree *tree = (BinaryTree *)malloc(sizeof(BinaryTree));
    tree->root = root;
    insert(tree, 8);
    insert(tree, 5);
    insert(tree, 2);
    insert(tree, 6);
    insert(tree, 10);
    insert(tree, 9);
    insert(tree, 11);
    printTree(tree->root);
}

