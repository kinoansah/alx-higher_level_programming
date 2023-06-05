#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s
{
	int data;
	struct listint_s *next;
}
listint_t: int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->nextnext;

		if (slow == fast)
		{
			return 1;	/* Cycle found */
		}
	}
	return 0;	/* No cycle found */
}

int main(void)
{
	/* Example usage */
	listint_t *list = malloc(sizeof(listint_t));
	list->data = 1;
	list->next = malloc(sizeof(listint_t));
	list->next->data = 2;
	list->next->next = malloc(sizeof(listint_t));
	list->next->next->data = 3;
	list->next->next->next = NULL;

	/* Creating a cycle */
	list-next->next->next = list->next;

	int hasCycle = check_cycle(list);
	printf("Has cycle: %d\n", hasCycle);

	/* Freeing memory */
	list->next->next->next = NULL;
	free(list->next->next);
	free(list->next);
	free(list);

	return (0);
}
