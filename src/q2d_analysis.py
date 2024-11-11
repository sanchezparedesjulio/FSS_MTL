# src/q2d_analysis.py

from pyaedt import Hfss
import os
import time
import pandas as pd
from config.variables_q2d import *  # Asegúrate de que estas variables están bien definidas en variables_q2d.py

def run_q2d_analysis():  # Asegúrate de que esta función se llama exactamente 'run_q2d_analysis'
    """
    Función que realiza el análisis Q2D de la FSS (Frequency Selective Surface).
    Establece parámetros geométricos, propiedades de materiales, configura la simulación,
    ejecuta el análisis y exporta los resultados en un archivo CSV.
    """

    # Crear el nombre del proyecto y directorio de resultados
    project_name = Q2D_PROJECT_NAME
    workspace_path = Q2D_WORKSPACE_PATH
    export_file = Q2D_EXPORT_FILE
    
    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(workspace_path):
        os.makedirs(workspace_path)
    
    # Inicializar el entorno de AEDT
    with Hfss() as hfss:
        # Crear un nuevo proyecto
        hfss.new_project()
        
        # Crear un nuevo diseño
        design = hfss.insert_design(project_name)

        # Aquí iría la creación de la geometría de la FSS
        # Ejemplo: Crea la celda FSS y sus componentes
        # fss_cell = hfss.create_rectangle(...)  # Usar la función para crear la geometría de la celda FSS
        
        # Aquí puedes añadir la creación de los "fingers" u otras estructuras dentro de la celda
        # Por ejemplo:
        # for i in range(N):
        #     hfss.create_rectangle(...)  # Crear los dedos o dipolos dentro de la geometría
        
        # Aquí se podrían crear más geometrías para las capas o componentes adicionales
        # Crear la estructura 3D o 2D según lo que sea necesario

        # Añadir las condiciones de frontera y excitación
        # En este caso, puedes asignar el puerto de onda (Wave Port)
        # Ejemplo:
        # hfss.assign_waveport(name="Port1", location=(0, 0, 0))  # Asignar un puerto para la simulación

        # Configuración de la simulación
        hfss.set_frequency(frequency_start=FREQ_START, frequency_end=FREQ_END, frequency_resolution=LAMBDA_RES)

        # Ejecutar la simulación
        hfss.solve()

        # Esperar a que la simulación termine
        while not hfss.is_solved():
            time.sleep(2)

        # Obtener los resultados de la simulación
        results = hfss.get_results()

        # Exportar los resultados a un archivo CSV
        results_data = pd.DataFrame(results)
        results_data.to_csv(os.path.join(workspace_path, export_file), index=False)

        print(f"Análisis Q2D completado. Los resultados se han exportado a {export_file}.")
        
        return results_data

# Llamada a la función
if __name__ == "__main__":
    run_q2d_analysis()  # Ahora ejecutas la función run_q2d_analysis