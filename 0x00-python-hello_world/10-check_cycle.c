#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Entry Point to the program
 * Description: Checks to see if a singly-linked list contains a cycle.
 * @list: Type of list
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1
 */
int check_cycle(listint_t *head)
{
	int *a, *b;

	if (head == NULL)
		return (0);

	while (head != NULL)
	{
		a = (int *)&head;
		b = (int *)&head->next;
		if (head->next == NULL)
			return (0);

		if (*a - *b <= 0)
			return (1);

		head = head->next;
	}
	return (0);
}
