### Remote debugging

<img width="729" alt="Screenshot 2024-06-24 at 12 53 47 PM" src="https://github.com/debamitra/debs-notes/assets/2363934/9c7deec2-a950-447d-a47c-2e4a06c0adda">



Internals of GDB
- GDB uses `ptrace` system call to observe and control the execution of another process and examine and change the process' memory and registers
- A breakpoint is implemented by replacing an instruction in memory with a special instruction which causes SIGTRAP
  
