#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head node
 * @number: the new inseted value
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	unsigned int i;
	listint_t *temp, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	temp = *head;
	for (i = 0; temp != NULL && number > temp->next->n; i++)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}
