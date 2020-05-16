#include <pthread.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 

pthread_t tid[2]; 
pthread_mutex_t lock; 

void* myFunction(void* arg) {

	pthread_mutex_lock(&lock); 
	
	int* val = (int *)arg;

	if(*val == 0) {
		printf("Hello World\n");
	}
	
	else if (*val == 1) {
		printf("Goodbye World\n");
	}
	
	pthread_mutex_unlock(&lock); 
	sleep(1);

	return NULL; 
} 

int main() {
 
	int i = 0;  

	while(1) {
		i = 0;
		while (i < 2) { 
			pthread_create(&(tid[i]), NULL, &myFunction, (void *)&i); 
			pthread_join(tid[i], NULL); 
			i++; 
		} 
	}
	
	pthread_mutex_destroy(&lock); 

	return 0; 
} 

