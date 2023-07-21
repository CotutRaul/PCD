#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  // definirea argumentelor pentru programul execve
  char *args[] = { "/bin/ls", "-l", NULL };
  
  // definirea mediului pentru programul execve
  char *envp[] = { "PATH=/bin", NULL };
  
  // apelarea functiei execve
  execve("/bin/ls", args, envp);
  
  // daca functia execve intoarce un rezultat negativ, afisam un mesaj de eroare
  perror("execve");
  return 1;
}