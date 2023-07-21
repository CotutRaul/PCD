#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  // definirea argumentelor pentru programul execv
  char *args[] = { "/bin/ls", "-l", NULL };
  
  // apelarea functiei execv
  execv("/bin/ls", args);
  
  // daca functia execv intoarce un rezultat negativ, afisam un mesaj de eroare
  perror("execv");
  return 1;
}