#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define NAME 256
#define SIZE 10

typedef struct hash_node
{
    char name[NAME];
    int age;
    struct hash_node *next;
    //other information about person
} hash_node;

hash_node *hash_map[SIZE];

unsigned int hash(char *value)
{
    unsigned int result = 0;
    for (int i = 0; strcmp(&value[i], "\0") != 0; i++)
    {
        result += value[i];
        result *= value[i];
    }
    return result % SIZE;
}

void init_hash_table(void)
{
    for (int i = 0; i < SIZE; i++)
    {
        hash_map[i] = NULL;
    }
}

void print_hash_table(void)
{
    printf("Start\n");
    for (int i = 0; i < SIZE; i++)
    {
        if (hash_map[i] != NULL)
        {
            hash_node *next1 = hash_map[i];
            printf("\t%d\t", i);
            while (next1 != NULL)
            {
                printf("%s -> ", next1->name);
                next1 = next1->next;
            }
            printf("NULL\n");
        }
        else
            printf("\t%d\t--\n", i);
    }
}

void insert_in_hash_map(hash_node *value)
{
    unsigned int index = hash(value->name);
    if (hash_map[index] == NULL)
        hash_map[index] = value;
    else
    {
        hash_node *current = hash_map[index];
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = value;
    }
}

hash_node *hash_table_lookup(char *name)
{
    unsigned int index = hash(name);
    if (hash_map[index] == NULL)
        return NULL;
    hash_node *ptr = hash_map[index];
    while (ptr != NULL)
    {
        printf("%s\n", ptr->name);
        if (strcmp(ptr->name, name) == 0)
            return ptr;
        ptr = ptr->next;
    }
    return NULL;
}

bool hash_table_delete(char *name)
{
    unsigned int index = hash(name);
    if (strcmp(hash_map[index]->name, name) == 0)
    {
        hash_map[index] = hash_map[index]->next;
        return true;
    }
    else if( hash_map[index] != NULL)
    {
        hash_node *ptr = hash_map[index];
        while (ptr != NULL)
        {
            if (strcmp(hash_map[index]->name, name) == 0)
            {
                ptr = NULL;
                return true;
            }
            ptr = ptr->next;
        }
    }
    return false;
        
}

int main(void)
{
    init_hash_table();
    hash_node a = { "Vlad", 17, NULL};
    hash_node c = { "Denys", 44, NULL};
    hash_node d = { "Taras", 23, NULL};
    hash_node b = { "123", 121, NULL};
    hash_node f = { "Monay", 99, NULL};
    hash_node g = { "Jasyi", 100, NULL};
    hash_node h = { "Artem", 454, NULL};
    hash_node i = { "John", 10, NULL};

    insert_in_hash_map(&a);
    insert_in_hash_map(&c);
    insert_in_hash_map(&b);
    insert_in_hash_map(&d);
    insert_in_hash_map(&h);
    insert_in_hash_map(&g);
    insert_in_hash_map(&i);
    insert_in_hash_map(&f);
    print_hash_table();
    if (hash_table_lookup("Vlad") != false)
        printf("Vlad was found!\n");
    else
        printf("Vlad wasn't found\n");
    hash_table_delete("Vlad");
    print_hash_table();
    return (0);
}