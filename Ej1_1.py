import psutil

try:
    notepad = False
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid

        print(processName, " --> ", processID)

        if processName.lower() == "notepad.exe":
            notepad = True

except:
    print("error")

if notepad == True:
    print("\n-El bloc de notas está en ejecución-")