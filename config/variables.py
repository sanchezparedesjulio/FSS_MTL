# config/variables_generales
import math
## Global constants
mu0 = 4 * math.pi * 1e-7               # Magnetic permeability of free space (H/m)
eps0 = 8.85418 * 1e-12                 # Permittivity of free space (F/m)
c0 = 1 / math.sqrt(eps0 * mu0)         # Speed of light in free space (m/s)
mm = 1e-3                              # Conversion from millimeters to meters
cm = 1e-2                              # Conversion from centimeters to meters
GHz = 1e9                              # Conversion from GHz to Hz


# config/variables_q2d.py
# Geometric parameters for the FSS (Frequency Selective Surface)
FSS_WIDTH = 0.5                        # Width of the FSS cell (m)
FSS_HEIGHT = 0.5                       # Height of the FSS cell (m)
FSS_THICKNESS = 0.01                   # Thickness of the FSS structure (m)

## Variables for geometry design
N = 4                                  # Number of fingers in the top layer of the FSS
M = 4                                  # Number of output fingers in the FSS
Nb = 2                                 # Number of parallel bondings in the FSS (for future WB configuration)

# Geometric dimensions for cell and dipole design (in mm)
# Cell dimensions
gx = 7                                  # X dimension of the cell in mm
gy = 7                                  # Y dimension of the cell in mm
Zlen = 30                               # Z dimension of the cell in mm

# Dipole parameters
T = 0.032                               # Metallization thickness in mm
Lf_1 = 5.9                              # Length of the first finger in mm
Lf_2 = 5.66                             # Length of the second finger in mm
Lf_3 = 5.5                              # Length of the third finger in mm
desp = 0.7                              # Separation between fingers in mm
sep = 0.6                               # Separation between layers in mm
Wf1 = 0.5                               # Width of finger 1 in mm
Wf2 = 0.4                               # Width of finger 2 in mm
Wf3 = 0.4                               # Width of finger 3 in mm

# Parámetros del material
MATERIAL = "PEC"            # Material de la FSS (por defecto cobre)

# Parámetros de simulación
RESOLUTION = 450               # Resolución del análisis, por ejemplo en cantidad de puntos de malla
MAX_ITERATIONS = 100            # Número máximo de iteraciones para la convergencia de simulación
PRECISION = 1e-4               # Precisión deseada para la convergencia de la simulación
freq_start = 10 * GHz                  # Start frequency for analysis (Hz)
freq_end = 40 * GHz                    # End frequency for analysis (Hz)
lambda_res = c0 / freq_end             # Wavelength resolution (m), based on end frequency

# Configuración de exportación de resultados
EXPORT_RESULTS = True           # Booleano para activar o desactivar la exportación de resultados
EXPORT_FORMAT = "csv"           # Formato de exportación de datos (e.g., "csv", "txt")

# Configuraciones de interfaz PyAEDT
VERSION = "2023.2"              # Versión específica de PyAEDT a usar
USE_NON_GRAPHICAL = True        # Ejecutar en modo no gráfico para automatización