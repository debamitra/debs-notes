1. What is **turnaround time**?
     T <sub>completion</sub> - T <sub>arrival</sub>
2. FIFO , Shortest Job First(SJF), Shortest Time-to-completion First are some scheduling algorithms discussed
3. Preemptive(a running job can be stopped before finishing) vs Non-preemptive scheduling.
4. What is **response time**?
     T <sub>firstrun</sub> - T <sub>arrival</sub>
5. Round Robin Scheduling - Fairness
6. STF optimizes for turnaround time.
7. RR optimizes for response time.


### Linux Completely Fair Scheduler

1. What is the vruntime?
   - CFS picks process with lowest runtime
2. What is sched_latency? How long a process should run before considering switching.
3. What is min_granularity?
4. What is the **nice** parameter?
   -20 to +19
   Positive value is lower priority
   <img width="627" alt="Screenshot 2024-05-04 at 8 06 27 PM" src="https://github.com/debamitra/debs-notes/assets/2363934/54069fa9-e45f-4550-aa1a-98a23c2cd59f">
   <img width="606" alt="Screenshot 2024-05-04 at 8 06 13 PM" src="https://github.com/debamitra/debs-notes/assets/2363934/7dfa3404-d5ef-49b2-a5c0-7bf68bfb8e8a">

5. Running/Runnable processes are stored in a red-black tree for search efficiency.



