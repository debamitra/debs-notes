## Address Translation

1. One pair of REGISTERS per CPU - the base register and the bounds register
   - Implemented in hardware circuitry (address translation from virtual memory address to physical memory address
   - This can be called the MMU or Memory Management Unit
   - Base REG stores the starting physical address location
   - Bounds REG stores the address space size of the process ( virtual memory addresses start from 0 to bounds)

2. The free list is a data strcuture that stores the address ranges which are unused in memory

3. OS issues:
   - OS must find space for the process address space in memory by - searching free list, then mark the space as used (fixed size address space? )
   - Set base/Bounds REGs on context switch
   - Exception handling (illegal memory access, illegal instruction )
  
REMIND ME : WHat is **return-from-trap instruction** - switching from kernel to user mode
