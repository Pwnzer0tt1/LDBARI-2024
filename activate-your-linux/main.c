#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>

bool check_key(char* buff, unsigned long n){
  if ( n != 18 ) return false;
  if ( buff[0] != 'H' ) return false; // H 
  if ( buff[0] + buff[1] != 'l' ) return false; // $
  if ((buff[1] ^ buff[2]) < 90 ) return false; // x
  if ( buff[2] * buff[3] != 6120 ) return false; // 3
  if ( buff[4] - buff[5] != 1 ) return false; // BA CB .. 
  if ( buff[6] % 50 != 5) return false; // 7 i 
  if (strcmp(buff + 8, "love-linux") != 0)  return false;
  return true;
}

int main() {
  setvbuf(stdout, NULL, _IONBF, 0);
  char buff[100] = {0};

  puts("Hello! Your linux license is about to expire!\n");
  puts("Please enter your activation key: ");
  
  scanf("%99s", buff);  

  unsigned long n = strlen(buff); 
  printf("You said %s. Length: %lu \n" , buff, n);

  if (check_key(buff,n)) {
    FILE * f = fopen("flag.txt", "r");
    char flag[100] = {0}; 
    fgets(flag, 100, f); 
    printf("Congrats! Here's your flag: %s", flag);
  } else {
    puts("Womp womp... Try again later!");
  }
  return 0;
}
