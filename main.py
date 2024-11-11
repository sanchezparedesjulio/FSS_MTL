# main.py

from src.q2d_analysis import run_q2d_analysis  # Importa la función para el análisis Q2D
from src.config_q2d import q2d  # Importa las configuraciones específicas para Q2D
from config.variables import FSS_WIDTH, FSS_HEIGHT, FSS_THICKNESS  # Variables generales del proyecto
import argparse

def main():
    """
    Función principal del programa que coordina los análisis de Q2D.
    """
    # Crear el objeto parser para gestionar argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description="Selecciona el tipo de análisis para el proyecto FSS")

    # Añadir los argumentos que acepta el programa
    parser.add_argument(
        '--analysis',  # El nombre del argumento
        choices=['Q2D'],  # Sólo permitimos análisis Q2D por ahora
        default='Q2D',  # Valor por defecto
        help='Selecciona el tipo de análisis (actualmente solo Q2D está soportado)'  # Descripción
    )

    # Parsear los argumentos
    args = parser.parse_args()

    # Comprobar qué tipo de análisis seleccionó el usuario
    if args.analysis == 'Q2D':
        print("Ejecutando análisis Q2D...")
        # Aquí llamas a la función para ejecutar el análisis Q2D
        run_q2d_analysis(q2d)  # Pasa las configuraciones de Q2D al análisis
    else:
        print("Error: Tipo de análisis no soportado.")

if __name__ == "__main__":
    main()