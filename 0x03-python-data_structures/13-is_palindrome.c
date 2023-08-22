#include "lists.h"
#include <stdio.h>

/**
 * count - elemnts number of the linked list
 * @head: head node
 * Return: number of elements
 */

int count(listint_t *head)
{
	if (head == NULL)
		return (0);

	return (1 + count(head->next));
}

/**
 * reverse_listint - function that reverses a listint_t linked list.
 * @head: pointer to the linked list
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev_node = NULL, *next_node = NULL;

	while (*head != NULL)
	{
		next_node = (*head)->next;
		(*head)->next = prev_node;
		prev_node = *head;
		*head = next_node;
	}

	*head = prev_node;

	return (*head);
}

/**
 * is_palindrome -checks if a singly linked list is a palindrome.
 * @head: head node
 * Return: 0 if not ot 1 if it is
 */

int is_palindrome(listint_t **head)
{
	int num_of_elemnts = count(*head);
	int i = 0, l, f_data, l_data;
	listint_t *first, *last;

	if (num_of_elemnts == 0)
		return (1);

	first = *head;
	while (i != num_of_elemnts / 2)
	{
		i++;
		f_data = first->n;
		last = *head;
		for (l = 0; l < num_of_elemnts - (i - 1); l++)
		{
			l_data = last->n;
			last = last->next;
		}
		if (f_data != l_data)
			return (0);
		first = first->next;
	}

	return (1);
}
