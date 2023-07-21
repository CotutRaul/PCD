#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  // definirea mediului pentru programul execle
  char *envp[] = { "PATH=/bin", NULL };
  
  // apelarea functiei execle
  execle("/bin/ls", "ls", "-l", NULL, envp);
  
  // daca functia execle intoarce un rezultat negativ, afisam un mesaj de eroare
  perror("execle");
  return 1;
}