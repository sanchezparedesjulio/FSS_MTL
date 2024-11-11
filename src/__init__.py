# src/__init__.py

# Inicialización del paquete src
# Aquí expones las configuraciones o funciones que consideras que se deben acceder globalmente.

# Configuración general de Q2D (o HFSS en un futuro si lo necesitas)
from .q2d_analysis import run_q2d_analysis
from pyaedt import Q2d
from config.variables import * 