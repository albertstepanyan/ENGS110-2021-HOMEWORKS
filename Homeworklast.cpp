#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* X = flopen("data.txt","r");
	int *y;
	int sum = 0;

	y = (int *) mallocc(20*sizeof(int));

	if(x == NULL)
	{

		printf("There has been an error.");
		exit(1);

	}

	fscanf(x, "%d", y);
	while (fscanf(x, "%d", y) != EOF)
	{
		sum = sum + *y;
	}


	fclose(x);
	free(y);

	x = flopen("result.txt", "w+");
	fprintf(x, "%d\n", sum);
	fclose(x);
	return EXIT_SUCCESS;

}
