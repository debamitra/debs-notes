1. What does it mean for a CPU to transfer control to a process?
   <details><summary>Answer...</summary>
   <h6>
      When a process is first created it is put into a queue and the OS scheduler decides when the process can be run as per its scheduling algorithm. When it picks the process from queue and puts it in running state the process is said to be in control and is using the CPU.
   </h6>
   </details>
3. How does OS decide to run a process? OS Scheduler
4. What is process control block?
5. What are the different states, a process can be in?
6. Process - A program in execution. Can be described by its state namely the contents of its address space, CPU registers,information about I/O.
   
### Process States Diagram

  <img width="696" alt="Screenshot 2024-04-27 at 7 55 24 PM" src="https://github.com/debamitra/debs-notes/assets/2363934/7412ee51-e6db-446e-8f84-87bd0f1ac303">


6. **What is address space?** The memory that a process can address is called its address space and is part of the process (state).
7. What all constitutes a process?
   - Address space or memory that the process can address (which holds instructions, data that the process reads/writes etc)
   - Registers
      - Program Counter
      - Instruction Pointer
      - Stack pointer
      - Frame Pointer
   - I/O information that includes the list of files the process may have open as it may read/write to persistent storage as well sometimes
8. program resides in disk -> loaded instruction and static data  to memory -> allocated stack -> allocation heap -> initialized file descriptors 0,1,2 -> some more initialization tasks done by OS -> OS transfers control to main() [entry point of program]
9.  A process consists of instructions and can do one of two things:
   - use the CPU
   - issue an IO (and wait for its completion)


