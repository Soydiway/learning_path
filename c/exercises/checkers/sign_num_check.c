#include <stdio.h>

int main(void){
  double num;
  printf("Enter a number: ");
  scanf("%lf",&num);
  if (num > 0){
    printf("%f is positive\n",num);
  } else if (num < 0){
    printf("%f is negative\n",num);
  }

  else {
    printf("0 is zero :)\n");
  }
  
  return 0;
}
