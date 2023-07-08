#include <stdio.h>
#include <stdlib.h>
#include "linked_list.c"
#include <stdbool.h>

typedef struct Stack
{
    LinkedList *data;
    Node *top;
} Stack;

Stack *get_stack(void)
{
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    LinkedList *lst = (LinkedList *)malloc(sizeof(LinkedList));
    lst->head = NULL;
    lst->tail = NULL;
    lst->length = 0;
    stack->data = lst;
    stack->top = NULL;
    return stack;
}

void push(Stack *stack, char *item)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->value = item;
    node->next = NULL;
    stack->top = node;
    append_node(stack->data, &node);
}

Node *pop(Stack *stack)
{
    int length = stack->data->length;
    if (length > 0)
    {
        Node *node = delete_node(stack->data, length-1);
        if (length == 1)
            stack->top = NULL;
        else
            stack->top = stack->data->tail;
        return node;
    }
    return NULL;
}

Node *peek(Stack *stack)
{
    return stack->top;
}

bool is_empty(Stack *stack)
{
    if (stack->data->length > 0)
        return false;
    return true;
}

void free_stack(Stack *stack)
{
    if (stack != NULL)
    {
        free_list(stack->data);
        free(stack);
    }
}

int main(void)
{
    Stack *stack = get_stack();
    push(stack, "Hello world");
    printf("Peek = %s\n", peek(stack)->value);
    print_linked_list(stack->data);
    push(stack, "Hi");
    printf("Peek = %s\n", peek(stack)->value);
    print_linked_list(stack->data);
    push(stack, "Man");
    printf("Peek = %s\n", peek(stack)->value);
    print_linked_list(stack->data);    
    pop(stack);
    printf("Peek = %s\n", peek(stack)->value);
    print_linked_list(stack->data);
    pop(stack);
    printf("Peek = %s\n", peek(stack)->value);
    print_linked_list(stack->data);
    pop(stack);
    print_linked_list(stack->data);
    pop(stack);
    pop(stack);
    pop(stack);
    pop(stack);
    free_stack(stack);
}