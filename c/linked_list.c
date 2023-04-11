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
    // Node *ptr = lst->head;
    // while (ptr->next != NULL)
    //     ptr = ptr->next;
    // ptr->next = node;
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

void delete_node(LinkedList *lst, int index)
{
    if (lst->head == NULL)
        return ;
    else if (index >= lst->length || index < 0)
        return ;
    else if (index == 0)
    {
        lst->head = lst->head->next;
        return ;
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
    if (i == lst->length - 2)
        lst->tail = prev;
    prev->next = curr->next;
    lst->length--;
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
    Node i = {"Hello world", NULL};
    LinkedList lst = { &i, &i, 1};
    Node j = {"A", NULL};
    append_node(&lst, &j);
    Node k = {"B", NULL};
    append_node(&lst, &k);
    Node m = {"C", NULL};
    insert(&lst, &m, 1);
    Node w = {"D", NULL};
    insert(&lst, &w, 0);
    print_linked_list(&lst);
    delete_node(&lst, 4);
    print_linked_list(&lst);
    Node ll = {"H", NULL};
    insert(&lst, &ll, 2);
    print_linked_list(&lst);
    reverse_list(&lst);
    Node *tmp;
    unsigned int q = 0;
    while (q < lst.length)
    {
        printf("%d\n", q);
        tmp = get_node(&lst, q);
        if (tmp->next != NULL)
            printf("Next : %s\n", tmp->next->value);
        else
            printf("Next is NULL\n");
        q++;
    }
    print_linked_list(&lst);
}