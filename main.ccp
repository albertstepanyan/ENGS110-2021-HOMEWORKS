int main() {

	int x = 20;
	int tmp = 0;
	int a = 0, b=1, s=0;
	while(a+tmp<=x){
		tmp = a;
		a= a+b;
		b = tmp;
		s= s+a;
		printf("%d\n",a);
	}
	printf("sum=%d\n",s);
	intrem;
	int i = 0;
	int array[8];
	while(s!=0){
		rem = s % 2;
		s=s/2;
		array[i]=rem;
		// printf("%d",array[i]);
		i++
		//printf("%d",rem);
		//printf("\n");

	}

	for(int j = i;j>=0;j--)
	printf("%d",array[j]);


