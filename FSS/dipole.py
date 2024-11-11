# src/periodic_elements/dipole.py

class Dipole:
    def __init__(self, id_dipole, w, l, t, material):
        """
        Constructor del Dipole. Inicializa las dimensiones y la posición del dipolo.
        
        :param id: Identificador único para el dipolo (se pasa automáticamente).
        :param desp: Separación entre los dipolos.
        :param width: Ancho del dipolo.
        :param length: Longitud del dipolo.
        :param thickness: Grosor del dipolo.
        """
       

        self.id_dipole = id_dipole
        self.w = w 
        self.l = l 
        self.t = t 
        self.material = material 
    def __repr__(self):

         print(f"Dipole created with ID {self.id}, width {self.w}, length {self.l}, thickness {self.t}, material {self.material}.")
