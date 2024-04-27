# Questions and Concepts

1. **What does it mean for a CPU to transfer control to a process?**
   - When the CPU transfers control to a process, it begins executing the instructions of that process.

2. **How does the OS decide to run a process?**
   - The decision is made by the OS Scheduler, which selects processes based on scheduling algorithms and system priorities.

3. **What is a Process Control Block (PCB)?**
   - The Process Control Block is a data structure maintained by the OS to store all information about a process. This includes the process's state, program counter, CPU registers, memory limits, and more.

4. **What are the different states a process can be in?**
   - A process can typically be in one of several states: new, ready, running, waiting (or blocked), and terminated.

5. **Process Description**
   - A process is a program in execution and can be described by its state, namely the contents of its address space and CPU registers, and information about I/O.

### Process States Diagram
![Process States Diagram](https://github.com/debamitra/debs-notes/assets/2363934/7412ee51-e6db-446e-8f84-87bd0f1ac303)

6. **What is address space?**
   - Address space is the memory locations that a process can use to store and retrieve data. It includes program code, data, and the stack.

7. **Functions of a Process**
   - A process consists of instructions and can do one of two things:
     - Use the CPU
     - Issue an I/O operation and wait for its completion
