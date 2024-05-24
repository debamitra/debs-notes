### Debugging tools on Mac OS
1. lldb <program-name>
2. AddressSanitizer
   > gcc -fsanitize=address -g leak_program.c -o leak_program ./leak_program


malloc(), calloc() and free() are some library calls used in allocating and deallocating memory



   
