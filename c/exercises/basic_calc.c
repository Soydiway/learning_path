#include <stdio.h>

int main(void){
  int first_num;
  printf("Enter first number: ");
  scanf("%d",&first_num);
  int sec_num;
  printf("Enter second number: ");
  scanf("%d",&sec_num);
  //guys,i haven't learned control-flow operators yet,so... простите me,K?
  printf("%d + %d = %d\n",first_num,sec_num, first_num + sec_num);
  printf("%d - %d = %d\n",first_num,sec_num,first_num - sec_num);
  printf("%d × %d = %d\n",first_num,sec_num,first_num * sec_num);

  // here I написал (tried) classic algorithm для ceil (когда мы хотим round дробное number к bigger числу). Usually C-compiler just отрезают дробную часть (при операциях с int-type variables)
  printf("%d / %d = %d\n",first_num,sec_num,(first_num + sec_num - 1) / sec_num);

  
  //I don't know нужно ли написать эти 4 строчки в.. одну строку? я of course мог бы make another реализацию same operations за один function calling,but it would be очень tangled. So,не ругайте за тавтологию
  return 0;
}
