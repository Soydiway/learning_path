#include <stdio.h>

int main (void){
  float width;
  float length;
  printf("Enter the width of the rectangle (in cm) : ");
  scanf("%f",&width);
  printf("Enter the length of the rectangle (in cm): ");
  scanf("%f",&length);
  printf("The area of the rectangle equals to %.2fcm²\n",width * length);
  return 0;
}
