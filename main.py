# main.py

from src.q2d_analysis import run_q2d_analysis  # Importa la función para el análisis Q2D
from config.config_q2d import q2d  # Importa las configuraciones específicas para Q2D
from config.variables import FSS_WIDTH, FSS_HEIGHT, FSS_THICKNESS  # Variables generales del proyecto


def main():
  
        run_q2d_analysis()  # Pasa las configuraciones de Q2D al análisis


if __name__ == "__main__":
    main()