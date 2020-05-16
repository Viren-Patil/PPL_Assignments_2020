#include<stdio.h>
#include<unistd.h>

int func() {

	int arr[2] = {7, 1};
	arr[2] = 9;
	arr[3] = 0x00005555;
	arr[4] = 0x5555517b;
	
	return 0;
}

void virus() {

	char *shell[2];
	
    shell[0] = "/bin/sh";
   	shell[1] = NULL;

   	execve(shell[0], shell, NULL);
}

int main() {
	func();
	return 0;
}


