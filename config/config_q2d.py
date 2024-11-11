# config/config_q2d.py
from config.variables_q2d import *
from config.variables import *  # Importa constantes y variables globales
from pyaedt import Q2d
# Diccionario principal donde almacenaremos todas las configuraciones formateadas para Q2D
q2d  = Q2d(PROJECT_NAME, Q2D_DESIGN_NAME) #crear proyecto

# Configuración de los parámetros de la celda en mm
q2d["gx"] = str(gx) + "mm"
q2d["gy"] = str(gy) + "mm"
q2d["Zlen"] = str(Zlen) + "mm"

# Configuración de los parámetros de los dipolos en mm
q2d["T"] = str(T) + "mm"       # Grosor de la metalización
q2d["Lf_1"] = str(Lf_1) + "mm" # Longitud del primer dipolo
q2d["Lf_2"] = str(Lf_2) + "mm" # Longitud del segundo dipolo
q2d["Lf_3"] = str(Lf_3) + "mm" # Longitud del tercer dipolo
q2d["desp"] = str(desp) + "mm" # Separación entre dipolos
q2d["sep"] = str(sep) + "mm"   # Separación entre capas
q2d["Wf1"] = str(Wf1) + "mm"   # Ancho del primer dipolo
q2d["Wf2"] = str(Wf2) + "mm"   # Ancho del segundo dipolo
q2d["Wf3"] = str(Wf3) + "mm"   # Ancho del tercer dipolo

# Parámetros de simulación
q2d["RESOLUTION"] = RESOLUTION
q2d["MAX_ITERATIONS"] = MAX_ITERATIONS
q2d["PRECISION"] = PRECISION
q2d["freq_start"] = str(freq_start) + "Hz"
q2d["freq_end"] = str(freq_end) + "Hz"
q2d["lambda_res"] = str(lambda_res) + "m"

# Material de la FSS
q2d["MATERIAL"] = MATERIAL

# Configuración de exportación de resultados
q2d["EXPORT_RESULTS"] = EXPORT_RESULTS
q2d["EXPORT_FORMAT"] = EXPORT_FORMAT

# Configuración de PyAEDT
q2d["VERSION"] = VERSION
q2d["USE_NON_GRAPHICAL"] = USE_NON_GRAPHICAL


# Parámetros específicos del diseño FSS
q2d["N"] = N
q2d["M"] = M
q2d["Nb"] = Nb




# Validación de configuración (opcional)
def validate_config():
    # Realiza comprobaciones adicionales, por ejemplo, asegurarse de que la frecuencia esté en un rango razonable
    if freq_start < 1e9 or freq_end > 50e9:
        raise ValueError("La frecuencia debe estar entre 1 GHz y 50 GHz.")
    if gx <= 0 or gy <= 0:
        raise ValueError("Dimensiones de FSS no válidas, deben ser mayores que cero.")
    if not (0 < RESOLUTION <= 2000):
        raise ValueError("Resolución no válida, debe estar entre 1 y 2000.")
    print(" USER INFO: Configuración validada correctamente.")

# Llama a la validación al cargar el módulo
validate_config()