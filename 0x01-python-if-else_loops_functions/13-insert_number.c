#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a node in a sorted linked list
 * @head: the beginning of the list
 * @number: the number to include in the linked list
 * Return: a pointer to the new added node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *newnode;

newnode = malloc(sizeof(listint_t));
if (!newnode)
return (NULL);
newnode->n = number;
newnode->next = NULL;
	/* first condition in such a case the newnode integer is less than */
	/* the integer stored in the head of the linked list */
	/* this due to is a sorted list  so we need to check this */
if (!(*head) || number <= (*head)->n)
{
newnode->next = *(head);
return ((*head) = newnode);
}
	/* if last condition is not the case then:*/
while (*head)
{
		/* logically head and run the list to check if*/
		/* the integers stored in the next nodes are greater than*/
		/* the integer of the newnode*/
if (!(*head)->next || (*head)->next->n > number)
{
			/* in such a case newnode take the place of the node*/
			/* that follows the head IF is greater than (27) */
newnode->next = (*head)->next;
(*head)->next = newnode;
return (newnode);
}
head = &(*head)->next;
}
return (NULL);
}
