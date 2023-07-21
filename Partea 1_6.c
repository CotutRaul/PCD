#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  // apelarea functiei execlp
  execlp("ls", "ls", "-l", NULL);
  
  // daca functia execlp intoarce un rezultat negativ, afisam un mesaj de eroare
  perror("execlp");
  return 1;
}