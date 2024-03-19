#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a plaindrome.
 * @head : pointer to pointer to head of the linked list.
 *
 * Return: 1 if the linked list is palindrome or 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *from_begin, *from_end;
	int length = 0, i, j;

	if (*head == NULL)
		return (1);
	from_begin = *head;
	while (from_begin->next != NULL)
	{
		length += 1;
		from_begin = from_begin->next;
	}
	from_begin = *head;
	for (i = 0; i < length; i++)
	{
		from_end = *head;
		j = 0;
		while (j < length - (i + 1))
		{
			from_end = from_end->next;
			j++;
		}
		if (from_begin->n != from_end->n)
		{
			printf("%d\n", j);
			return (0);
		}
		printf("%d\n", from_begin->n);
		from_begin = from_begin->next;
	}
	return (1);
}
