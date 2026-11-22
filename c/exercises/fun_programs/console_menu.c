#include <stdio.h>

int run_calculator(void);

int main(void){
  int choice;
  printf("What next\n");

  printf("1. Print 'Hello wolrd'\n"
         "2. Run calculator\n"
         "3. Who am I?\n"
         "4. Quit\n"
         "Your choice: ");
  scanf("%d",&choice);

  switch(choice){

    case 1:
      printf("Hello world\n");
      break;
    case 2:
      run_calculator();
      break;
    case 3:
      printf("I'm just an intern, still learning the ropes\n");
    case 4:
      break;
    default:
      printf("Hey, you tried to do something that isn't  allowed in this program. That's not good >:(\n");
      break;
  }
  
}
