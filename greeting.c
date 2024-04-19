//Write a C program to print 'Welcome to C programming!
#include <stdio.h>

int main() {
    printf("Welcome to C Programming\n");
    return 0;
}







//Write a C program that prompts the user for their name and prints a personalized greeting.
#include <stdio.h>

int main() {
    char name[50]; // Assuming the name won't exceed 50 characters
    
    // Prompt the user for their name
    printf("Enter your name: ");
    scanf("%49s", name); // Read the name input from the user
    
    // Print personalized greeting
    printf("Hello, %s! Welcome to the program.\n", name);
    
    return 0;
}
