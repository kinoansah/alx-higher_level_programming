#include <stdio.h>
#include <stdlib.h>

/**
 * struct ListNode - singly linked list
 * @val: integer value
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct ListNode
{
    int val;
    struct ListNode *next;
} ListNode;

/**
 * reverseList - Reverses a linked list
 * @head: Pointer to the head of the linked list
 * Return: Pointer to the reversed list
 */
ListNode *reverseList(ListNode *head)
{
    ListNode *prev = NULL;
    ListNode *current = head;
    ListNode *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(ListNode *head)
{
    if (head == NULL || head->next == NULL)
        return 1;

    ListNode *slow = head;
    ListNode *fast = head;
    ListNode *prev = NULL;
    ListNode *second_half = NULL;

    // Find the middle of the list and reverse the second half
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        second_half = slow->next;
    }
    else
    {
        second_half = slow;
    }

    prev->next = NULL;
    second_half = reverseList(second_half);

    // Compare the first half and the reversed second half
    ListNode *p1 = head;
    ListNode *p2 = second_half;

    while (p1 != NULL && p2 != NULL)
    {
        if (p1->val != p2->val)
        {
            return 0;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    return 1;
}

/**
 * createNode - Creates a new node with the given value
 * @val: Value of the node
 * Return: Pointer to the newly created node
 */
ListNode *createNode(int val)
{
    ListNode *newNode = malloc(sizeof(ListNode));
    if (newNode == NULL)
    {
        perror("malloc");
        exit(EXIT_FAILURE);
    }
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

/**
 * createLinkedList - Creates a linked list from an array of values
 * @values: Array of integer values
 * @size: Size of the array
 * Return: Pointer to the head of the linked list
 */
ListNode *createLinkedList(int *values, int size)
{
    ListNode *head = NULL;
    ListNode *current = NULL;
    for (int i = 0; i < size; i++)
    {
        ListNode *newNode = createNode(values[i]);
        if (head == NULL)
        {
            head = newNode;
            current = newNode;
        }
        else
        {
            current->next = newNode;
            current = newNode;
        }
    }
    return head;
}

/**
 * freeLinkedList - Frees the memory allocated for a linked list
 * @head: Pointer to the head of the linked list
 */
void freeLinkedList(ListNode *head)
{
    while (head != NULL)
    {
        ListNode *temp = head;
        head = head->next;
        free(temp);
    }
}

int main(void)
{
    int values[] = {1, 2, 3, 2, 1};
    int size = sizeof(values) / sizeof(values[0]);

    ListNode *head = createLinkedList(values, size);

    int result = is_palindrome(head);

    printf("Is the linked list a palindrome? %s\n", result ? "Yes" : "No");

    freeLinkedList(head);

    return 0;
}
