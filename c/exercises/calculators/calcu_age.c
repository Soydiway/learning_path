#include <stdio.h>
#define CURRENT_YEAR 2026
#define CURRENT_MONTH 11
#define CURRENT_DAY 19

int main(void){
  int year_of_birth;
  int month_of_birth;
  int day_of_birth;
  printf("Enter your date of birth (DD MM YY) : ");
  scanf("%d%d%d",&day_of_birth,&month_of_birth,&year_of_birth);

  printf("%d\n",(CURRENT_YEAR - year_of_birth) - ((CURRENT_MONTH * 100 + CURRENT_DAY) < (month_of_birth * 100 + day_of_birth)));
  return 0;
}
