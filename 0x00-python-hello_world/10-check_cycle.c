#include "lists.h"

/**
 * check-cycle - Checks for loops in
 * linked lists
 * @list: The list in interest
 * Return: 1 if it's looped, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	/* make a fixed node and a moving node*/
	listint_t fixed = list, moving = list;

	/* iterate over the list */
	/* if the list isn't ended */
	while (moving->next)
	{
		/* and moving == fixed -> is cycled */
		if (moving == fixed)
			return (1);
		moving = moving->next;
	}
	/* Otherwise isn't cycled and return 0 */
	return (0);
}