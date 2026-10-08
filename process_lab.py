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