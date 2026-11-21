#include <stdio.h>

int main(void){
  int num;
  printf("Enter a number: ");
  scanf("%d",&num);
  printf("The number is %s\n", (num % 2 == 0) ?  "even" : "odd");
  return 0;
}
