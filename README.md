
# Práctica P3 - STP Claim Root Bridge
Viensy Pérez  
**Matrícula:** 20241203  

## Descripción
Repositorio individual para la práctica P3: ataque STP Claim Root Bridge en la asignatura Seguridad de Redes.  
El ataque envía BPDUs falsos para reclamar ser el root bridge en la red, forzando al switch a cambiar su topología y permitiendo al atacante manipular el flujo de tráfico.

## Archivos incluidos
- `Viensy_20241203_STP_P3.py` → Script en Python para el ataque.
- `Viensy_20241203_Informe_P3.pdf` → Informe con explicación, capturas y resultados.
- `capturas/` → Evidencias gráficas del ataque.
- `Viensy_20241203_P3.zip` → Paquete final con todos los entregables.

## Direccionamiento IP
El laboratorio utiliza direccionamiento basado en la matrícula:
- Red: `192.168.120.0/24`
- Router (R1): `192.168.120.1`
- Kali: `192.168.120.99`
- Switch: configurado con STP activo

## Ejecución del script
En Kali:
```bash
python3 Viensy_20241203_STP_P3.py
