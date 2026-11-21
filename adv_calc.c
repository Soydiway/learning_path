#include <stdio.h>

int main(void){
  int choice,f_operand,s_operand;
  printf("Enter two numbers (separated by space): ");
  scanf("%d%d",&f_operand,&s_operand);
  printf("+[1], - [2], × [3], ÷ [4]\nEnter operator number: ");
  scanf("%d",&choice);
  int result = (choice == 1) ? f_operand + s_operand :
               (choice == 2) ? f_operand - s_operand :
               (choice == 3) ? f_operand * s_operand :
               (choice == 4) ? ( (s_operand != 0) ? (f_operand + s_operand - 1) / s_operand  : printf("Error : division by zero. %d / %d <-- here\n",f_operand,s_operand) && 0) : 0;
  printf("Result: %d", result);
  printf(" %s\n",(choice == 4) ? (s_operand == 0) ? "(error)" : ( (double)f_operand / s_operand == f_operand / s_operand) ? "(not rounded)" : "(rounded up)" : "just number :)" );
  return 0;
}
