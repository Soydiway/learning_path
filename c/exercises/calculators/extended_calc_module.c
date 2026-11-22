#include <stdio.h>

int run_calculator (void){

  int f_num,s_num;
  char op;

  
  printf("Enter first number: ");
  scanf("%d",&f_num);

  printf("Enter second number: ");
  scanf("%d",&s_num);

  printf("Avalaible operations:\n"
         "1. multiplication (*)\n"
         "2. division (/)\n"
         "3. subtraction (-)\n"
         "4. addition (+)\n"
         "5. convert to percentage (%%)\n"
         "6. modulo operation (remainder,symbol: !)\n"
         "Enter your choice (symbol): ");
  scanf(" %c",&op);
  printf("Result is ");
  switch(op){
    case '*':
      printf("%d\n",f_num * s_num);
      break;
    case '/':
      if (s_num != 0){
        printf("%d\n",f_num / s_num);
      }
      else {
        printf("error: division by zero!\n");
      }
      break;
    case '-':
      printf("%d\n",f_num - s_num);
      break;
    case '+':
      printf("%d\n",f_num + s_num);
      break;
    case '%':
      printf("%d of %d equals %.2f%%\n",f_num,s_num, (f_num / (float)s_num) * 100);
      break;
    case '!':
      if(s_num != 0){
        printf("%d\n",f_num % s_num);
      }
      else {
        printf("error: division by zero!\n");
      }
      break;
    default:
      printf("none\nHey, enter a symbol of an existing operation! I don't know what '%c' is\n",op);
      break;
  }
  return 0;
}
