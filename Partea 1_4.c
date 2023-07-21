#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  // apelarea functiei execl
  execl("/bin/ls", "ls", "-l", NULL);
  
  // daca functia execl intoarce un rezultat negativ, afisam un mesaj de eroare
  perror("execl");
  return 1;
}