#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;
    }

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || number < (*head)->n) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    listint_t *current = *head;
    while (current->next != NULL && number > current->next->n) {
        current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;
    return new_node;
}

void print_list(listint_t *head) {
    while (head != NULL) {
        printf("%d ", head->n);
        head = head->next;
    }
    printf("\n");
}

int main() {
    listint_t *head = NULL;
    insert_node(&head, 10);
    insert_node(&head, 20);
    insert_node(&head, 30);
    insert_node(&head, 15);
    insert_node(&head, 25);

    print_list(head);

    return 0;
}

