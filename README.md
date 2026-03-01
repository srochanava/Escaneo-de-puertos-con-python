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

<img width="510" height="249" alt="ejemplo_portscanner" src="https://github.com/user-attachments/assets/012f292c-d55c-4ffc-8fa2-f28ca9b42c5f" />

## Advertencias importantes:

- Uso ético y legal: Solo escanea hosts que tú poseas o para los que tengas permiso explícito por escrito.
- Escanear redes o dispositivos sin autorización puede ser considerado un ataque y es ilegal en la mayoría de países.
- En redes corporativas o públicas, este tipo de escaneo suele ser detectado y puede generar alertas de seguridad.

## Limitaciones:

- Solo escanea puertos TCP
- No es multihilo → puede ser lento en rangos muy grandes (>5000 puertos)
- La detección de banner es básica y falla con muchos servicios modernos
- No soporta IPv6
