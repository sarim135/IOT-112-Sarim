//Write a C program to ask name from user and greet him
#include <stdio.h>

int main() {
    char name[50]; // Assuming the name won't exceed 50 characters
    
    // Prompt the user for their name
    printf("Enter your name: ");
    scanf("%49s", name); // Read the name input from the user
    
    // Print personalized greeting
    printf("Hello, %s! Welcome to the program.\n", name);
    fflush(stdout);

    
    return 0;
}
