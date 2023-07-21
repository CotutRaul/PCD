#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  // definirea argumentelor pentru programul execvp
  char *args[] = {"ls", "-l", NULL};

  // apelarea functiei execvp
  execvp("ls", args);

  // daca functia execvp intoarce un rezultat negativ, afisam un mesaj de eroare
  perror("execvp");
  return 1;
}