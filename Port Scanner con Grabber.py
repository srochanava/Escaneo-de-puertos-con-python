import socket

def main():
    # Solicitar datos al usuario
    print("=== Escáner de puertos simple ===\n")
    
    ip_objetivo = input("Ingresa la dirección IP a escanear: ").strip()
    
    while True:
        try:
            puerto_inicio = int(input("Puerto inicial (ej. 1): "))
            if puerto_inicio < 1 or puerto_inicio > 65535:
                print("El puerto debe estar entre 1 y 65535")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    while True:
        try:
            puerto_fin = int(input("Puerto final (ej. 1024): "))
            if puerto_fin < 1 or puerto_fin > 65535:
                print("El puerto debe estar entre 1 y 65535")
                continue
            if puerto_fin < puerto_inicio:
                print("El puerto final debe ser mayor o igual al inicial")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido")
    
    print(f"\nEscaneando {ip_objetivo} desde puerto {puerto_inicio} hasta {puerto_fin}...")
    print("-" * 60)
    
    puertos_abiertos = 0
    
    for puerto in range(puerto_inicio, puerto_fin + 1):
        try:
            # Creamos socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Tiempo máximo de espera (más rápido que el default)
            sock.settimeout(0.8)
            
            # Intentamos conectar
            resultado = sock.connect_ex((ip_objetivo, puerto))
            
            if resultado == 0:
                puertos_abiertos += 1
                print(f"Puerto {puerto:>5} → ABIERTO", end="")
                
                # Intentamos leer banner (opcional)
                try:
                    sock.settimeout(1.2)
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                    if banner:
                        print(f"  →  {banner}")
                    else:
                        print("  →  (sin banner)")
                except:
                    print("  →  (no se pudo obtener banner)")
                
            sock.close()
            
        except KeyboardInterrupt:
            print("\n\nEscaneo interrumpido por el usuario")
            break
        except:
            # Ignoramos otros errores silenciosamente
            pass
    
    print("-" * 60)
    print(f"\nEscaneo finalizado.")
    print(f"Se encontraron {puertos_abiertos} puerto(s) abierto(s)")
    print("Rastreo finalizado\n")


if __name__ == "__main__":
    main()
