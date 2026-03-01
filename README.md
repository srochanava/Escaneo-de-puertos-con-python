# Escaneo-de-puertos-con-python
Herramienta ligera escrita en Python para escanear puertos TCP abiertos en una dirección IP específica.   Con fines de aprendizaje, pruebas locales o diagnóstico básico de red.

**Características principales:**

- Escanea rangos de puertos personalizados (ej: 1–1024, 80–443, 3000–4000...)
- Solo muestra los **puertos abiertos**
- Intenta obtener el **banner** del servicio (cuando es posible)
- Validación de entrada del usuario (IP y puertos)
- Manejo de interrupción con Ctrl+C
- Mensaje final con resumen de puertos encontrados
- Muy liviano: solo usa la biblioteca estándar (`socket`)

## Requisitos:

- Python 3.6 o superior  
  (Funciona perfectamente en 3.8–3.12)

No requiere instalación de paquetes externos.

## Ejemplo de Ejecución:

    === Escáner de puertos simple ===
    
    Ingresa la dirección IP a escanear: 192.168.1.1
    Puerto inicial (ej. 1): 1
    Puerto final (ej. 1024): 100
    
    Escaneando 192.168.1.1 desde puerto 1 hasta 100
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    Puerto    22 → ABIERTO → SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
    Puerto    80 → ABIERTO → (sin banner)
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    Escaneo finalizado.
    Se encontraron 2 puerto(s) abierto(s)
    Rastreo finalizado


## Advertencias importantes:

- Uso ético y legal: Solo escanea hosts que tú poseas o para los que tengas permiso explícito por escrito.
- Escanear redes o dispositivos sin autorización puede ser considerado un ataque y es ilegal en la mayoría de países.
- En redes corporativas o públicas, este tipo de escaneo suele ser detectado y puede generar alertas de seguridad.

## Limitaciones:

- Solo escanea puertos TCP
- No es multihilo → puede ser lento en rangos muy grandes (>5000 puertos)
- La detección de banner es básica y falla con muchos servicios modernos
- No soporta IPv6
