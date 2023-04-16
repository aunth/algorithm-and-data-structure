#include <stdio.h>
#include "stdlib.h"

typedef struct Node
{
    char *value;
    struct Node *next;
} Node;

typedef struct LinkedList
{
    Node *head;
    Node *tail;
    unsigned int length;
} LinkedList;

LinkedList *get_list()
{
    LinkedList *lst = (LinkedList *) malloc(sizeof(LinkedList));
    lst->head = NULL;
    lst->length = 0;
    lst->tail = NULL;
    return lst;
}

Node *find(LinkedList *lst, int index)
{
    if (index >= lst->length || index < 0)
        return NULL;
    int i = 0;
    Node *current = lst->head;
    while (i != index)
    {
        i++;
        current = current->next;
    }
    return current;
}

void print_linked_list(LinkedList *lst)
{
    Node *ptr = lst->head;
    if (ptr == NULL)
    {
        printf("NULL\n");
        return ;
    }
    while (ptr->next != NULL)
    {
        printf("%s -> ", ptr->value);
        ptr = ptr->next;
    }
    printf("%s -> NULL\n", ptr->value);
}

Node *get_node(char *value)
{
    Node *node = (Node *) malloc(sizeof(Node));
    node->value = value;
    node->next = NULL;
    return node;
}

void append_node(LinkedList *lst, Node *node)
{
    if (lst->head == NULL)
    {
        lst->head = node;
        lst->tail = lst->head;
    }
    else
    {
        lst->tail->next = node;
        lst->tail = node;
    }
    lst->length++;
}

void insert(LinkedList *lst, Node *node, int index)
{
    int i = 0;
    if (index == 0)
    {
        node->next = lst->head;
        lst->head = node;
        lst->length++;
        return ;
    }
    else if (index >= lst->length)
    {
        append_node(lst, node);
        return ;
    }    
    Node *ptr = lst->head;
    while (i < index - 1)
    {
        ptr = ptr->next;
        i++;
    }
    node->next = ptr->next;
    ptr->next = node;
    lst->length++;
}

Node *delete_node(LinkedList *lst, int index)
{
    if (lst->head == NULL)
        return NULL;
    else if (index >= lst->length || index < 0)
        return NULL;
    else if (index == 0)
    {
        Node *result = lst->head;
        lst->head = lst->head->next;
        lst->length--;
        return result;
    }
    int i = 1;
    Node *prev = lst->head;
    Node *curr = lst->head->next;
    while (i < index)
    {
        i++;
        prev = curr;
        curr = curr->next;
    }
    if (i == lst->length - 1)
        lst->tail = prev;
    prev->next = curr->next;
    lst->length--;
    return curr;
}

void reverse_list(LinkedList *lst)
{
    if (lst->length == 1)
        return ;
    Node *first = lst->head;
    lst->tail = lst->head;
    Node *second = first->next;
    Node *tmp;
    while (second)
    {
        tmp = second->next;
        second->next = first;
        first = second;
        second = tmp;
    }
    lst->head->next = NULL;
    lst->head = first;
}

void free_list(LinkedList *lst) {
    Node *current = lst->head;
    Node *next;
    while (current != NULL) 
    {
        next = current->next;
        free(current);
        current = next;
    }
    free(lst);
}

// int main(void)
// {
//     LinkedList *lst = get_list();
//     Node *a = get_node("A");
//     append_node(lst, a);
//     print_linked_list(lst);
//     Node *b = get_node("B");
//     Node *c = get_node("C");
//     Node *d = get_node("D");
//     Node *e = get_node("E");
//     Node *f = get_node("F");
//     append_node(lst, b);
//     print_linked_list(lst);
//     append_node(lst, c);
//     print_linked_list(lst);
//     delete_node(lst, lst->length-1);
//     print_linked_list(lst);
//     free_list(lst);
//     return 0;
// }