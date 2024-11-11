Proyecto FSS: Simulación de Superficies Selectivas de Frecuencia (FSS)

Este proyecto utiliza la librería PyAEDT para diseñar y analizar estructuras de Superficie Selectiva de Frecuencia (FSS), enfocándose inicialmente en una estructura 3+2 (3 capas de entrada y 2 capas de salida). Se prevé que el proyecto evolucione para soportar configuraciones de estructura N+M, donde el número de capas de entrada y salida será configurable.

Tabla de Contenidos

1. Descripción General
2. Instalación y Requisitos
3. Estructura de Carpetas
4. Uso
5. Versiones
6. Contribuciones
7. Licencia

---

Descripción General

Este proyecto permite realizar el análisis electromagnético de estructuras FSS utilizando el software HFSS y Q2D. Su objetivo es proporcionar un flujo de trabajo flexible para el diseño, análisis y exportación de resultados de simulaciones en diferentes configuraciones de FSS.

El proyecto tiene como objetivo expandirse para soportar configuraciones N+M, donde N representa el número de capas en la entrada y M el número de capas de salida.

Instalación y Requisitos

Para usar el proyecto, es necesario tener instalados:

- Python 3.8+
- PyAEDT 2023+ para interactuar con HFSS y Q2D.
- Visual Studio Code (opcional), recomendado para desarrollo y organización del proyecto.

Estructura de Carpetas

La organización de las carpetas y archivos del proyecto es la siguiente:

Proyecto_FSS/
├── config/                 # Configuración y variables del proyecto
│   ├── variables_q2d.py    # Archivo de variables específicas de la simulación 2D
│   └── config_q2d.py       # Archivo de configuración para Q2D
│
├── analysis_modules/       # Módulos de análisis
│   ├── hfss_analysis.py    # Análisis electromagnético usando HFSS
│   └── q2d_analysis.py     # Análisis usando Q2D
│
├── main.py                 # Script principal para ejecutar el proyecto
├── README.md               # Documentación general del proyecto
└── requirements.txt        # Dependencias del proyecto

Uso

Para ejecutar el proyecto, sigue los pasos a continuación:

1. Configurar Variables:
   - Las variables geométricas, materiales y de simulación se definen en config/variables_q2d.py.
   - Estas configuraciones se aplican automáticamente al ejecutar cualquiera de los análisis.

2. Ejecutar Simulación HFSS o Q2D:
   - Selecciona en main.py el tipo de análisis (HFSS o Q2D) configurando el tipo de análisis requerido.
   - Ejecuta el análisis:
     python main.py
   - Los resultados se exportarán en el formato especificado en config/variables_q2d.py.

Versiones

Versión Actual: 1.0.0

- Configuración Inicial: Este primer lanzamiento soporta estructuras 3+2 (3 capas de entrada y 2 capas de salida).
- Análisis Disponibles:
  - Análisis electromagnético con HFSS.
  - Análisis electrostático con Q2D.
- Exportación de Resultados: Los resultados se pueden exportar en formato CSV.

Próximas Versiones:

- Versión 1.1.0 (Planificada)
  - Mejora de la estructura para soportar configuraciones N+M.
  - Implementación de un selector de análisis para elegir entre HFSS y Q2D desde la línea de comandos.
  - Funcionalidad para seleccionar diferentes materiales y espesores en cada capa de la FSS.

- Versión 1.2.0 (Planificada)
  - Soporte para exportar resultados en múltiples formatos (e.g., JSON, TXT).
  - Documentación ampliada para la personalización de estructuras complejas de FSS.
  - Integración de opciones de simulación avanzadas (p. ej., número de iteraciones y precisión de malla) desde la interfaz de configuración.

Contribuciones

Para contribuir al proyecto:

1. Haz un fork del repositorio.
2. Crea una rama para tus contribuciones: git checkout -b feature/nueva-funcionalidad
3. Realiza tus modificaciones.
4. Envía un pull request con una descripción detallada de los cambios realizados.

Información Adicional

Para cualquier duda o mejora, no dudes en abrir una issue en el repositorio del proyecto.