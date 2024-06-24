### Remote debugging

<img width="715" alt="Screenshot 2024-06-24 at 12 57 17 PM" src="https://github.com/debamitra/debs-notes/assets/2363934/56aaffa4-14c6-4e26-8e86-4bd7aecfe466">





Internals of GDB
- GDB uses `ptrace` system call to observe and control the execution of another process and examine and change the process' memory and registers
- A breakpoint is implemented by replacing an instruction in memory with a special instruction which causes SIGTRAP
  
