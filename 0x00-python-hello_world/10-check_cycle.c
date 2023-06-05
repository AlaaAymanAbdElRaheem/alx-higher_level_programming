#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it.
 * @list: head of the list
 * Return: 0 (no cycle) or 1 (there is a cycle).
 */

int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	s = list;
	f = list;

	if (list == NULL)
		return (0);

	while (f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}

	return (0);
}
