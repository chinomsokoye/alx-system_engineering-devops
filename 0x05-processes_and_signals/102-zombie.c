#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Entry point
 * Return: Always 0
 */
int main(void)
{
	int i = 0;
	pid_t zombie;

	while (i < 5)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
		i++;
	}
	infinite_while();
	return (0);
}
