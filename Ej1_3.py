import psutil

try:
    for proc in psutil.process_iter():
        processName = proc.name()
        processCPU = proc.cpu_percent()
        processMemory = proc.memory_percent()

        print(f"{processName}, uso de CPU: {processCPU}%, uso de memoria: {processMemory}%")

except:
    print("error")
