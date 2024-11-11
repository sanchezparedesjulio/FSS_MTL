# src/__init__.py

# Inicialización del paquete src
# Aquí expones las configuraciones o funciones que consideras que se deben acceder globalmente.

# Configuración general de Q2D (o HFSS en un futuro si lo necesitas)
from config_q2d import q2d  # Accede directamente a las configuraciones de Q2D

# Exponer las funciones de análisis o los módulos que son fundamentales en el flujo general del programa
from q2d_analysis import run_q2d_analysis  # Importa correctamente la función 'run_q2d_analysis'
from geometry import create_geometry  # Si tienes funciones de geometría que necesitas usar globalmente

# Aquí también podrías exponer las variables de configuración globales si son necesarias a nivel global
from variables import *