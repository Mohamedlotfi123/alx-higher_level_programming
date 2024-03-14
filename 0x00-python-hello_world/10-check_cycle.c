#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check if a single linked list has a cycle
 * @list : pointer to the list
 *
 * Return: 1 if the list has a cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	if (list == NULL)
		return (0);
	head = list;
	while (head->next != NULL)
	{
		head = head->next;
		if (list->n == head->n)
		{
			return (1);
		}
	}
	return (0);
}
