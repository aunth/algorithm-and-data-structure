#include <stdio.h>

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

Node *get_node(LinkedList *lst, int index)
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
    while (ptr->next != NULL)
    {
        printf("%s -> ", ptr->value);
        ptr = ptr->next;
    }
    printf("%s -> NULL\n", ptr->value);
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
    while (i < index-1)
    {
        i++;
        prev = curr;
        curr = curr->next;
    }
    if (i == lst->length - 2)
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

int main(void)
{
    LinkedList lst = { NULL, NULL, 1};
    Node a = {"A", NULL};
    append_node(&lst, &a);
    Node b = {"B", NULL};
    Node c = {"C", NULL};
    Node d = {"D", NULL};
    Node e = {"E", NULL};
    Node f = {"F", NULL};
    append_node(&lst, &b);
    printf("Top is  %s\n", lst.tail->value);
    print_linked_list(&lst);
    printf("Head is %s, tail is %s\n", lst.head->value, lst.tail->value);
    append_node(&lst, &c);
    printf("Top is  %s\n", lst.tail->value);
    print_linked_list(&lst);
    printf("Head is %s, tail is %s\n", lst.head->value, lst.tail->value);
    append_node(&lst, &d);
    printf("Top is  %s\n", lst.tail->value);
    print_linked_list(&lst); 
    printf("Head is %s, tail is %s\n", lst.head->value, lst.tail->value);
    append_node(&lst, &e);
    printf("Top is  %s\n", lst.tail->value);
    print_linked_list(&lst);
    printf("Head is %s, tail is %s\n", lst.head->value, lst.tail->value);
    append_node(&lst, &f);
    printf("Top is  %s\n", lst.tail->value);
    print_linked_list(&lst);
    printf("Head is %s, tail is %s\n", lst.head->value, lst.tail->value);
    printf("Deliting..\n");
    delete_node(&lst, lst.length-1);
    print_linked_list(&lst);
    delete_node(&lst, lst.length-1);
    print_linked_list(&lst);
    insert(&lst, &f, 2);
    print_linked_list(&lst);
    return 0;
}