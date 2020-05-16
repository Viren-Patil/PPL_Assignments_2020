#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void *functionName(void *arg) {
	
	while(1) {
		printf("Hello\n");
		sleep(1);
	}
	
	return NULL;
}

int main() {

	pthread_t thread_id;
	pthread_create(&thread_id, NULL, functionName, NULL);
	pthread_join(thread_id, NULL);
	
	return 0;
}
