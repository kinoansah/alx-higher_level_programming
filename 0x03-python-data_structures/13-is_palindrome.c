#include "lists.h"

/**
 * reverse - Reverses a singly linked list *
 * @h_r: Double pointer to the head of the list
 *
 * Description: Reverses the order of the nodes in a singly linked list.
 * Return: no return
 */
void reverse(listint_t **h_r)
{
	listint_t *prv;
	listint_t *crr;
	listint_t *nxt;

	prv = NULL;
	crr = *h_r;

	while (crr != NULL)
	{
		nxt = crr->next;
		crr->next = prv;
		prv = crr;
		crr = nxt;
	}

	*h_r = prv;
}

/**
 * compare - Compares the values of two singly linked lists *
 * @h1: Pointer to the head of the first list
 * @h2: Pointer to the head of the second list
 *
 * Return: 1 if the lists have the same values in the same order, 0 otherwise
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - Checks if a singly linked list
 * is a palindrome
 * @head: Double pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		isp = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (isp);
}
