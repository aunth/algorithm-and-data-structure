#include "linked_list.c"
#include <stdbool.h>

typedef struct Queue
{
    LinkedList *data;
    Node *first;
} Queue;

Queue *get_queue(void)
{
    Queue *queue = (Queue *) malloc(sizeof(Queue));
    LinkedList *lst = get_list();
    queue->data = lst;
    queue->first = 0;
    return queue;
}

void enqueue(Queue *queue, char *value)
{
    Node *new_node = get_node(value);
    if (queue->data->length == 0)
        queue->first = new_node;
    insert(queue->data, new_node, queue->data->length);
}

Node *dequeue(Queue *queue)
{
    if (queue->data->length > 0)
    {
        Node *removed = delete_node(queue->data, 0);
        if (queue->data->length > 0)
            queue->first = queue->first->next;
        else
            queue->first = NULL;
        return removed;
    }
    return NULL;
}

bool if_empty(Queue *queue)
{
    if (queue->first != NULL)
        return false;
    return true;
}

Node *peek(Queue *queue)
{
    return queue->first;
}

void free_queue(Queue *queue)
{
    if (queue != NULL)
    {
        free_list(queue->data);
        free(queue);
    }
}

int main(void)
{
    Queue *queue = get_queue();
    enqueue(queue, "A");
    printf("%s\n", peek(queue)->value);
    print_linked_list(queue->data);
    enqueue(queue, "B"); 
    print_linked_list(queue->data);
    printf("%s\n", peek(queue)->value);
    enqueue(queue, "C");
    print_linked_list(queue->data);
    printf("%s\n", peek(queue)->value);
    dequeue(queue);
    printf("%s\n", peek(queue)->value);
    print_linked_list(queue->data);
    dequeue(queue);
    printf("%s\n", peek(queue)->value);
    print_linked_list(queue->data);
    dequeue(queue);
    print_linked_list(queue->data);
}





