### Debugging tools on Mac OS
1. lldb <program-name>
2. AddressSanitizer
   > gcc -fsanitize=address -g leak_program.c -o leak_program ./leak_program


malloc(), calloc() and free() are some library calls used in allocating and deallocating memory



### System calls used for memory allocation
1. **brk/sbrk** are used for small memory allocation needs.
   - brk : sets the end of a data segment (**data segment** is the part of the address space which is reserved for dynamic memory allocation) to a specified value , changing the allocated amount of memory.
   - sbrk : increments the programs data space by a specified amount

2. **nmap** generally used to map files or devices into memory but can also be used to allocate memory with the 'MAP_ANONYMOUS' flag which means the memory is not backed by a file. Its often used for large memory allocations.
3. **munmap** is used to unmap previosuly mapped memory region and release it back to the system
