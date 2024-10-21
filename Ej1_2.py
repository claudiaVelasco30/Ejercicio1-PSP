import psutil

try:
    pid = int(input("Introduce el PID del proceso que quieras finalizar: "))

    for proc in psutil.process_iter():
        if proc.pid == pid:
            proc.terminate()
            print("El proceso ", proc.name(), " ha terminado")

except ValueError:
    print("PID incorrecto")
except psutil.NoSuchProcess:
    print("El proceso no existe")
except psutil.AccessDenied:
    print("No tienes permisos para finalizar este proceso")
except:
    print("No se pudo finalizar el proceso")