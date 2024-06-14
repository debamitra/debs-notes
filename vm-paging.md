
### Understanding Page Tables and Memory Management

1. **Byte-Addressable Memory**:
   - In a byte-addressable memory system, each unique address points to one byte of memory.
   - A 32-bit address space means that each address in memory is represented by 32 bits, allowing for 2^32 unique addresses.
   - So 2^32 bytes of memory can be addressed with a 32-bit address. (2^32 bytes = 4GB)

2. **Pages and Page Size**:
   - Virtual Memory is divided into small, fixed-size blocks called pages.
   - For example if each page is 4KB (kilobytes) in size, where 1KB = 1024 bytes, so 4KB = 4096 bytes.
   - So each page needs 4096 addresses to address 4096 bytes in the page
   - How many bits would the address need? 12 bits ( since, 2^12 = 4096 )

3. **Virtual Address Structure**:
   - A virtual address is divided into two parts: the Virtual Page Number (VPN) and the offset.
   - **VPN**: Identifies which page we are talking about.
   - **Offset**: Identifies the exact byte within that page.


   **Offset Calculation**:
   - A 4KB page size means we need 12 bits to represent the offset within the page (since 2^12 = 4096 bytes = 4KB).
   - This 12-bit offset allows us to address each individual byte within the 4KB page.

   **VPN Calculation**:
   - The remaining bits (32 - 12 = 20 bits) represent the VPN.
   - With 20 bits we can have how many pages? 2^20 = 1,048,576 (little more than 1 million pages)


4. **Page Table Size**
   - Each entry in the page table needs to store information about one page.
   - Typically, each PTE is 4 bytes (32 bits), which includes the physical frame number and some control bits.
   - With a million pages, and each entry being 4 bytes, the total size of the page table is:
   1,048,576 pages × 4 bytes/page = 4,194,304 bytes ≈ 4 MB
   - For 100 processes, the total memory required is:
     100 processes × 4 MB/process = 400 MB


### Whats in the Page Table?
e.g. x86 page table entry (32 bits)
<img width="887" alt="Screenshot 2024-06-14 at 1 35 12 PM" src="https://github.com/debamitra/debs-notes/assets/2363934/d7c2ebac-7a77-494f-a629-35c5e228b9a4">



 





