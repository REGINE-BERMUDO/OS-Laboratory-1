# OS-Laboratory-1

**Operating Systems – Process Management**

---

## Objective

Create and run a simple Python program in GitHub Codespaces, then use Linux commands (`ps`, `grep`, `top`) to observe process creation, PIDs, process states, the Process Control Block (PCB), and multiple processes.

## Tools Used

- GitHub account and GitHub Codespaces
- Python 3
- Linux terminal commands: `ps`, `ps aux`, `grep`, `top`

**Python version:** `Python 3.14.2`

---

## The Program (`process_lab.py`)

```python
import os
import time

print("==========================================")
print("       OPERATING SYSTEMS LABORATORY")
print("       PROCESS MONITORING ACTIVITY")
print("==========================================")

pid = os.getpid()

print("Process ID (PID):", pid)
print("Process has been created.")
print("Process is executing...")
print()

for i in range(1, 16):
    print("Execution step:", i)
    time.sleep(2)

print()
print("Process execution completed.")
print("Process is terminating...")
```

---

## Procedure and Results

### Part F – Process ID

Ran `python3 process_lab.py` and recorded the PID printed by the program.

**Q: Why does the operating system assign a PID to every process?**

- The PID is a unique number that identifies each process. The OS uses it to track, schedule, and control the process, and to tell apart processes that run the same program.

### Part G – `ps` and `ps aux`

While the program was running, a second terminal was used to run `ps` and `ps aux`.

| Information | Observation |
| --- | --- |
| PID | 15105 |
| CPU % | 0.1 |
| Memory % | 0.1 |
| User | codespa+ |
| Command | python3 process_lab.py |

### Part H – Searching with `grep`

Command: `ps aux | grep process_lab`

**Q: How does the grep command help us locate a specific process?**

- `ps aux` lists many processes. `grep process_lab` filters the list so only lines containing "process_lab" are shown, which makes it easy to find one specific process along with its PID, CPU, and memory use.

### Part I – Process States

Command used: `ps -e -o pid,stat,cmd | grep process_lab`

I used `-e` and `grep` because the program was running in a different terminal. The plain `ps -o pid,stat,cmd` only lists processes from the current terminal, while `-e` lists processes from all terminals and `grep` filters the output to my process.

| Process | PID | STAT | Meaning |
| --- | --- | --- | --- |
| python3 process_lab.py | 22154 | S+ | Sleeping, foreground |

The process was in the **S (Interruptible Sleep)** state because it waits during `time.sleep(2)` between execution steps. The `ps` command itself showed **R+** (Running).

| Code | Meaning |
| --- | --- |
| R | Running/Runnable |
| S | Interruptible Sleep |
| D | Uninterruptible Sleep |
| T | Stopped |
| Z | Zombie |

### Part J – Monitoring with `top`

| Observe | Result |
| --- | --- |
| PID | 33395 |
| CPU utilization | 0.0% |
| Memory utilization | 0.1% |
| Process state | S (Interruptible Sleep) |
| Process name | python3 (running `process_lab.py`) |

In `top`, the process showed almost no CPU use because it spends most of its time waiting during `time.sleep(2)`. The summary at the top showed 28 total tasks, with 1 running and 27 sleeping.

### Part K – Relating the Activity to the PCB

**Q: Which information observed using `ps` and `top` could be associated with information maintained by the operating system for a process?**

| PCB field | Seen in ps/top |
| --- | --- |
| Process ID | PID |
| Process State | STAT / S column |
| CPU Context | Not shown |
| Scheduling Info | %CPU, PR (priority), NI (nice value) |
| Memory Info | %MEM, VIRT, RES |
| I/O Information | Not shown |

The PID, process state, CPU usage, and memory usage shown by `ps` and `top` match information the OS keeps in the PCB. The user and command are also tracked for each process. `ps` and `top` only show selected information, not the complete PCB.

### Part L – Multiple Processes

Ran `python3 process_lab.py` in three terminals, then ran `ps aux | grep process_lab` in a fourth terminal.

| Process | PID | State | CPU % |
| --- | --- | --- | --- |
| Process 1 | 4910 | S+ | 0.4 |
| Process 2 | 4926 | S+ | 0.0 |
| Process 3 | 4956 | S+ | 0.4 |

#### Analysis Questions

1. **Are the PIDs the same?**
   No. The three processes have different PIDs: 4910, 4926, and 4956.
2. **Why are the PIDs different?**
   Each running copy of the program is a separate process, and the OS gives every process its own unique PID so it can identify, track, and manage each one.
3. **Are the three processes running the same program?**
   Yes. All three run the same program, `process_lab.py`, but each is a separate process with its own PID, state, and PCB.
4. **Can one program create multiple processes?**
   Yes. Running the same program several times creates several processes, each with its own PID, memory, and CPU context.
5. **Who manages these processes?**
   The operating system. It creates the processes, assigns PIDs, keeps a PCB for each one, schedules them on the CPU, and switches between them (context switching).
---

## Conclusion

In this activity I created a Python program, ran it in GitHub Codespaces, and used `ps`, `grep`, and `top` to observe its PID, state, CPU use, and memory use. The program was mostly in the sleeping (S) state because it waits during `time.sleep(2)`. Running it three times created three separate processes with different PIDs. This showed that the operating system creates, schedules, and manages each process using a PCB, and switches the CPU between processes through context switching.