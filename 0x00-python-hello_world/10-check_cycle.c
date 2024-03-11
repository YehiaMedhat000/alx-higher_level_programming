#include "lists.h"

/**
 * check_cycle - Checks for loops in
 * linked lists
 * @list: The list in interest
 * Return: 1 if it's looped, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	/* make a slow node and a fast node*/
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);

	while (fast && slow && fast->next)
	{
		fast = (fast->next)->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	/* Otherwise isn't cycled and return 0 */
	return (0);
}
