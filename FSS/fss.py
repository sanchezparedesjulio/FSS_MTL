# src/fss/fss.py

from periodic_elements.dipole import Dipole  # Importa la clase Dipole o cualquier otro elemento resonante
from config.variables_q2d import *  # Importa las variables de configuración de Q2D
from config.variables_hfss import *  # Importa las variables de configuración de HFSS
from analyses.q2d_analysis import run_q2d_analysis  # Importa la función para análisis Q2D
from analyses.hfss_analysis import run_hfss_analysis  # Importa la función para análisis HFSS

class FSS:
    """
    Clase que representa una estructura FSS (Frequency Selective Surface) que contiene 
    N elementos resonantes, donde cada uno está en una capa diferente.
    La clase almacena los parámetros como las dimensiones de la caja de radiación, 
    las capas y los elementos resonantes.
    """
    
    def __init__(self, n_layers, resonant_element_type, box_dimensions):
        """
        Constructor de la clase FSS. No se crea ninguna geometría en este momento.
        
        :param n_layers: Número de capas en la FSS (el número de elementos resonantes).
        :param resonant_element_type: Tipo de elemento resonante (por ejemplo, Dipole).
        :param box_dimensions: Dimensiones de la caja de radiación (como un diccionario o tupla).
        """
        self.n_layers = n_layers  # Número de capas (elementos resonantes)
        self.resonant_element_type = resonant_element_type  # Tipo de elemento resonante (Dipole, etc.)
        self.box_dimensions = box_dimensions  # Dimensiones de la caja de radiación
        self.layers = []  # Lista para almacenar las capas y sus elementos
        self.results = None  # Para almacenar los resultados de la simulación

    def create_layers(self):
        """
        Crear las capas de la FSS, cada una con un elemento resonante.
        Dependiendo del tipo de elemento resonante, se inicializa la clase correspondiente.
        """
        for i in range(self.n_layers):
            # Crear un elemento resonante según el tipo especificado (en este caso, un Dipole)
            element = self.resonant_element_type()  # Esto creará una instancia de la clase, como Dipole()
            self.layers.append(element)
        
        print(f"Se han creado {len(self.layers)} capas con {self.resonant_element_type.__name__} como elemento resonante.")

    def analyze_q2d(self):
        """
        Ejecuta el análisis Q2D para la FSS.
        """
        print(f"Iniciando análisis Q2D para la FSS con {self.n_layers} capas.")
        self.results = run_q2d_analysis(self)  # Llamada a la función de análisis Q2D
    
    def analyze_hfss(self):
        """
        Ejecuta el análisis HFSS para la FSS.
        """
        print(f"Iniciando análisis HFSS para la FSS con {self.n_layers} capas.")
        self.results = run_hfss_analysis(self)  # Llamada a la función de análisis HFSS

    def export_results(self, export_path):
        """
        Exportar los resultados de la simulación a un archivo.

        :param export_path: Ruta donde se guardarán los resultados.
        """
        if self.results:
            with open(export_path, 'w') as file:
                file.write(str(self.results))  # Exporta los resultados (puedes cambiar el formato a CSV, por ejemplo)
            print(f"Resultados exportados a: {export_path}")
        else:
            print("No hay resultados para exportar.")