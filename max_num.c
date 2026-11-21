#include <stdio.h>

int main(void){
  int f_num,s_num,th_num;
  printf("Enter three numbers: ");
  scanf("%d%d%d",&f_num,&s_num,&th_num);
  int greatest = (f_num > s_num) ? f_num : s_num;
  greatest = (greatest > th_num) ? greatest : th_num;
  printf("Largest number: %d\n",greatest);
  return 0;
}
