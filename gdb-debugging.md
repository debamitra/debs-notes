### Remote debugging


<img width="925" alt="Screenshot 2024-06-23 at 2 51 04 PM" src="https://github.com/debamitra/debs-notes/assets/2363934/4e978e02-1fc3-45fe-b17f-840709a95e06">

Internals of GDB
- GDB uses `ptrace` system call to observe and control the execution of another process and examine and change the process' memory and registers
- A breakpoint is implemented by replacing an instruction in memory with a special instruction which causes SIGTRAP
  
