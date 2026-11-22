#include <stdio.h>
#define F(x) (x * 9 / 5 + 32)
#define K(x) (x + 273.15)
#define Ra(x) ( (x + 273.15) * 9 / 5)
#define Re(x) (x * 4 / 5)
int main (void){
  
  float Celsius;
  
  printf("Enter temperature (degrees Celsius): ");
  scanf("%f",&Celsius);

  printf("Temperature in degrees Fahrenheit: %f\n",F(Celsius));
  printf("Temperature in Kelvins: %f\n",K(Celsius));
  printf("Temperature in degrees Rankine: %f\n",Ra(Celsius));
  printf("Temperature in degrees Reaumur: %f\n",Re(Celsius));
  return 0;
}
