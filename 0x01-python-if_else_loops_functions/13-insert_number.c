#include "lists.h"

/**
 * insert_node - Inserts a node in
 * a sorted linked list
 * @head: The head node of the list
 * @number: The number to put in the new node
 * Return: The address of the new node
 * NULL in failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;

	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node->next && node && node->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);
}
