#include <stdio.h> 
#include <pthread.h> 
#include <semaphore.h> 
#include <unistd.h> 
#include <stdlib.h>
#include <time.h>
  
int hr, min, sec;
sem_t mutex; 
pthread_t t[3];

void* thread(void* arg) 
{ 
    //wait 
    sem_wait(&mutex);
    int *val = (int *)arg; 
	
	if(*val == 0) {
		while (sec < 60) {
			sleep(1);
			system("clear");
			printf("\t\t\t\t\t%02d:%02d:%02d\n", hr, min, sec);
			sec++;
		}
	}
	
	else if(*val == 1) {
		sec = 0;
		min += 1;
	}
	
	else if(*val == 2) {
		if (min >= 60) {
			min = 0;
			hr += 1;
		}
		
		if(hr >= 24) {
			hr = 0;
			min = 0;
			sec = 0;
		}
	}
	
    
    sem_post(&mutex); 
}


int main() {
 	
	time_t rawtime;
	struct tm * timeinfo;
	time(&rawtime);
	timeinfo = localtime(&rawtime);
	hr = timeinfo->tm_hour;
	min = timeinfo->tm_min; 
	sec = timeinfo->tm_sec;
    sem_init(&mutex, 0, 1); 
    int i = 0;
    while(1) {
    
    	i = 0;
    	while(i < 3) { 
    		pthread_create(&t[i],NULL,thread,(void*)&i); 
    		pthread_join(t[i],NULL); 
    		i++;
    	}
    	
    }
    
    sem_destroy(&mutex); 
    return 0; 
} 
