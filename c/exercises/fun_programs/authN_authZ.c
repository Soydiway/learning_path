#include <stdio.h>
#include <string.h>
#define ADMIN_ID 38894092
#define ADMIN_PW 88467009
#define RANDOM_DUDE_ID 29383829
#define RANDOM_DUDE_PW 30082719
#define J_EPSTEIN_ID 00000000
#define J_EPSTEIN_PW 11111111
// just an authorization program... exercise.
// FOR THE UK READERS!!! IT'S IMPORTANT :
// just an authorisation program... exercise.



int main(void){

  int role = 2;
  int user_id;
  int user_pw;
  char who;
  char secret_pw[32];
  
  printf("Are you new to the system? [y/n]\t");
  scanf("%c", &who);

  if (who == 'Y' || who == 'y'){
    user_id = 20292849;
    user_pw = 44736882;
    printf("Then welcome!\n"
           "Your ID is %d and your password is %d\n",user_id,user_pw);
  } else if(who == 'N' || who == 'n'){
  
    printf("Enter ID to sign in (8 digits): ");
    scanf("%d", &user_id);
    printf("Enter a password: ");
    scanf("%d", &user_pw);

    switch(user_id){

      case ADMIN_ID:
        if(user_pw == ADMIN_PW){
          printf("Welcome!\n");
          role = 0;
        }
        else {
          printf("Wrong password!\n");
        }
        break;
      case RANDOM_DUDE_ID:
        if(user_pw == RANDOM_DUDE_PW){
          printf("Welcome!\n");
          role = 1;
        }
        else {
          printf("Wrong password!\n");
        }
        break;
      case J_EPSTEIN_ID:
        if(user_pw == J_EPSTEIN_PW){
          printf("Welgone!\n");
        }
        else{

          (void)getchar();
          printf("Hey, did you forget the password? Then enter the secret password: ");
          if(fgets(secret_pw,sizeof(secret_pw),stdin) != NULL){
            secret_pw[strcspn(secret_pw,"\n")] = '\0';

            if(strcmp(secret_pw,"I am subhuman") == 0){
              printf("I know\n");
            }
            else {
              printf("You typed it wrong\nHint: the secret password is 'I am subhuman'\n");
            }
            
          }
          else {
            printf("Uh... something's wrong with the input system\n");
          }

          
        }
        break;

        default:
          printf("Uhm.. who is %d?\n",user_id);
          break;
        
    }
    
  }
    
  else {
    printf("Yea bro, I know that there are other keys except 'n' and 'y' but just follow the instructions, K? +_-\n");
  }
  if (role == 0){
    printf("You're the admin, so do whatever you want\n");
  }
  else if(role == 1){
    printf("O child of Israel, I am God YHWH.\n"
           "I command you to do the following:\n"
           "1. Pray to me every day (not required at night)\n"
           "2. Do not eat pork (unless offered)\n"
           "3. Always start a purchase deal with the minimum amount (if you are seller,start with the maximum)\n"
           "4. Deceiving people is a sin (nobody is without sin)\n"
           "!!!For breaking my commandments, the punishment will be eternal torment in hell!!!\n"
           "Admission to heaven: 500 shekels\n"
           "Admin panel in heaven: 4,000 shekels\n"
           "Cheat mode in heaven: 9,999 shekels\n"
           "Become God: 600,000 shekels\n");
  }
  else{
    printf("Actually, you don't have a role, so get out\n");
  }
  return 0;
}
