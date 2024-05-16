1. How is the PID generated?
2. To think - is there a limit to no of processes that can exist concurrently because of the limit in max PID? Possibly limits are more on resources like memory limitations etc.
3. What are the system calls used to create a process in UNIX?
4. What is a system call?
   - file management system calls
   - process control
   - communication
   - device manipulation
  
5. fork() creates exact copy of calling process which continues by returning from fork() system call.
6. exec() loads code from executable and overwrites its current code segment with it
7. What is a code segment?
8. How do pipes work in unix?
   - While the theoretical limit on the number of pipes is set by the available file descriptors( if its 1024 then ~500 etc), practical usage is often constrained by broader system resource considerations and the requirements of the specific application
10. What are signals ?
11. What are process groups?
12. What are interrupts?

13. **What is a file descriptor?**
    - a non-negative interger that uniquely identifies an opened file or I/O resource within a process
    - Every process has its own file descriptors table. Each file descriptor entry in the table points to a file handle that represents an open file or I/O resource, e.g., the standard output, a pipe, etc.
    - To think - since file descriptors for all processes point to same stdin, stdout and stderr, what happns when many processes simulteneusly print to stdout. How does it work for stdin? - each terminal or program which starts the process has its own stdin/stdout associated with it. What exactly is stdin/stdout? They are streams, each process has its own set of streams to which it binds to.
      
    ![File Descriptor Image](https://github.com/debamitra/debs-notes/assets/2363934/51415b79-863c-4e40-a763-d0a78e576db9)

14. **How does the dup2() system call work?**
    - Example: `dup2(pipefd[1], STDOUT_FILENO);`

    **Before the Duplication:**
    - `STDOUT_FILENO` points to a file descriptor entry associated with the terminal or console output.
    - `pipefd[1]` points to a file descriptor entry that is part of the pipe's write mechanism.

    ```
    File Descriptor Table
    ----------------------
    0 -> Standard Input (stdin)
    1 -> Standard Output (stdout, typically your terminal or console)
    2 -> Standard Error (stderr)
    ... (other entries)
    pipefd[0] -> Read end of a pipe
    pipefd[1] -> Write end of a pipe
    ```

    **After the Duplication:**
    - Both `STDOUT_FILENO` and `pipefd[1]` point to the same entry: the write end of the pipe.
    - The original entry that `STDOUT_FILENO` pointed to (usually the terminal or console output) is no longer linked to `STDOUT_FILENO`. It has been closed as part of the dup2 operation if it was open.

    ```
    File Descriptor Table
    ----------------------
    0 -> Standard Input (stdin)
    1 -> Write end of a pipe (same as pipefd[1])
    2 -> Standard Error (stderr)
    ... (other entries)
    pipefd[0] -> Read end of a pipe
    pipefd[1] -> Write end of a pipe (same as STDOUT_FILENO)
    ```


