#include <stdio.h>

int main(void){
  int overall_percentage;
  printf("Enter overall percentage: ");
  scanf("%d",&overall_percentage);

  printf("Grade: ");

  
  if (overall_percentage >= 90){

    
    if (overall_percentage >= 97){
      printf("A+\n");
    } else if(overall_percentage >= 93){
      printf("A\n");
    }
    else {
      printf("A-\n");
    }


  } else if(overall_percentage >= 80){


    if(overall_percentage >= 87){
      printf("B+\n");
    } else if (overall_percentage >= 83){
      printf("B\n");
    }
    else {
      printf("B-\n");
    }

    
  } else if (overall_percentage >= 70){


    if(overall_percentage >= 77){
      printf("C+\n");
    } else if (overall_percentage >= 73){
      printf("C\n");
    }
    else {
      printf("C-\n");
    }

    
  } else if (overall_percentage >= 60){


    if(overall_percentage >= 67){
      printf("D+\n");
    } else if (overall_percentage >= 63){
      printf("D\n");
    }
    else {
      printf("D-\n");
    }

    
  } else {

    printf("F\n");
    
  }


  
  return 0;
}
