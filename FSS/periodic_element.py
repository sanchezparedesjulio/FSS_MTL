import warnings
from config.variables import Wf, Lf  # Suponiendo que los valores están definidos en config/variables.py

class PeriodicElement:
    def __init__(self, id_element, n_elements, desp, desp_z, box_dimensions, element_type=Dipole):
        """
        Constructor de la clase PeriodicElement. Define un conjunto de elementos en una capa periódica.

        :param id_element: Identificador de la capa o elemento.
        :param n_elements: Número de elementos en la capa.
        :param desp: Distancia de separación entre los elementos en el eje X y Y.
        :param desp_z: Distancia de separación entre los elementos en el eje Z.
        :param box_dimensions: Dimensiones máximas de la caja de radiación [x, y, z].
        :param element_type: Tipo de elemento resonante (e.g., Dipole).
        """
        self.id_element = id_element
        self.n_elements = n_elements
        self.desp = desp  # Distancia de separación entre elementos en el plano X-Y
        self.desp_z = desp_z  # Distancia de separación entre elementos en el eje Z
        self.box_dimensions = box_dimensions  # [x, y, z] como lista
        self.element_type = element_type  # Puede ser una clase como Dipole
        self.elements = []  # Lista para almacenar los elementos en la capa

        # Verificar si los elementos exceden las dimensiones de la caja de radiación
        self.check_dimensions()

    def check_dimensions(self):
        """
        Verifica si los elementos exceden las dimensiones de la caja de radiación. Si es así, muestra un warning.
        """
        # Calcular el tamaño total de la estructura dependiendo de si es un número impar o par de elementos
        if self.n_elements % 2 == 1:
            total_width = self.n_elements * self.element_type.width + (self.n_elements - 1) * self.desp
        else:
            total_width = self.n_elements * self.element_type.width + (self.n_elements) * self.desp

        total_height = self.element_type.length
        total_depth = self.element_type.thickness  # Suponiendo que el espesor del dipolo es la "profundidad" en el eje Z

        # Verificar si el tamaño excede la caja en cualquiera de los tres ejes
        if total_width > self.box_dimensions[0]:
            warnings.warn(f"Warning: The total width of {total_width} exceeds the box width of {self.box_dimensions[0]}.")

        if total_height > self.box_dimensions[1]:
            warnings.warn(f"Warning: The total height of {total_height} exceeds the box height of {self.box_dimensions[1]}.")

        if total_depth > self.box_dimensions[2]:
            warnings.warn(f"Warning: The total depth of {total_depth} exceeds the box depth of {self.box_dimensions[2]}.")

    def create_elements(self):
        """
        Crea los elementos dentro de la capa, considerando la distancia de separación en X, Y, y Z.
        """
        # Calcular el desplazamiento inicial de X para que los dipolos estén centrados
        offset_x = 0  # El desplazamiento inicial en X depende de la paridad de los elementos

        # Calcular la posición inicial en X para que la estructura esté centrada
        if self.n_elements % 2 == 1:
            offset_x = -(self.n_elements // 2) * (Wf[0] + self.desp)  # Para números impares
        else:
            offset_x = -(self.n_elements // 2 - 1) * (Wf[0] + self.desp)  # Para números pares

        # Crear los elementos (ejemplo con Dipole)
        for i in range(self.n_elements):
            # Posición en Z, desplazada por el parámetro desp_z
            Zpos = i * self.desp_z  # Posición en Z para cada elemento (desplazamiento entre los dipolos en Z)

            # Calcular la posición de X, dependiendo de si el número de dipolos es impar o par
            Xpos = offset_x + (i // 2) * (Wf[0] + self.desp)  # Posición en X considerando el ancho de cada dipolo y desp

            # Cálculo para el desplazamiento en Y (centro en Y del dipolo, empezando en l/2)
            Ypos = -self.element_type.length/ 2  # 

            # Calcular el índice para acceder a Wf y Lf según si es par o impar
            index = i if i % 2 == 0 else i - 1  # Usar el índice adecuado (0, 2, 4...) para los anchos (Wf)
            w_index = index // 2  # Índice para acceder a Wf
            l_index = index // 2  # Índice para acceder a Lf

            # Obtener el valor de ancho (w) y largo (l) del dipolo usando los índices calculados
            w = Wf[w_index]  # Ancho del dipolo
            l = Lf[l_index]  # Largo del dipolo

            # Grosor y material (de acuerdo a la clase Dipole)
            t = self.element_type.thickness  # Grosor (t) de acuerdo a la clase Dipole
            material = self.element_type.material  # Material del dipolo (definido en la clase)

            # Crear el elemento (dipolo)
            element = self.element_type(i, w, l, t, Xpos, Ypos, Zpos, material)  # Crear un elemento del tipo especificado (e.g., Dipole)
            self.elements.append(element)

        print(f"{len(self.elements)} elements created with type {self.element_type.__name__}.")