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
	int *p1, *p2;

	if (head == NULL)
		return (0);

	while (head != NULL)
	{
		p1 = (int *)&head;
		p2 = (int *)&head->next;
		if (head->next == NULL)
			return (0);

		if (*p1 - *p2 <= 0)
			return (1);

		head = head->next;
	}
	return (0);
}
