# src/periodic_elements/dipole.py

class Dipole:
    def __init__(self,P_ansys,Type_ansys, id_dipole, w, l, t ,Xpos,Ypos,Zpos,material="PEC"):
        """
        Constructor del Dipole. Inicializa las dimensiones y la posición del dipolo.
        
        :param P_ansys: Parámetro relacionado con la API de Ansys.
        :param Type_ansys: Indica si el dipolo se crea en un entorno 'Q2D' o 'HFSS'.
        :param id_dipole: Identificador único para el dipolo.
        :param w: Ancho del dipolo.
        :param l: Longitud del dipolo.
        :param t: Grosor del dipolo.
        :param Xpos: Posición en el eje X.
        :param Ypos: Posición en el eje Y.
        :param Zpos: Posición en el eje Z.
        :param material: Material del dipolo (por defecto es PEC).
        """
        self.P_ansys = P_ansys #manejador de HFSS o Q2D
        self.T_ansys = T_ansys
        self.id_dipole = id_dipole#puede ser que no sea nada
        self.id_ansys= None
        self.w = w 
        self.l = l 
        self.t = t 
        self.material = material
        #en vez de esto puedo poner origin y despues calcular end
        self.Xpos = Xpos 
        self.Ypos = Ypos 
        self.Zpos = Zpos 
    def __repr__(self):

        print(f"Dipole created with ID {self.id}, width {self.w}, length {self.l}, thickness {self.t}, material {self.material}.")
    
    def create_in_ansys(self):
        """
        Crea el dipolo en Ansys (HFSS o Q2D) y asigna `id_ansys` tras la creación.
        """
        if self.Type_ansys == "Q2D":
            # Llamada de creación para Q2D
            self.id_ansys = self.P_ansys.create_q2d_dipole()
        elif self.Type_ansys == "HFSS":
            # Llamada de creación para HFSS
            self.id_ansys = self.P_ansys.create_hfss_dipole()
        else:
            raise ValueError("Tipo de Ansys no reconocido: debe ser 'Q2D' o 'HFSS'.")

        print(f"Dipolo creado en {self.Type_ansys} con ID: {self.id_ansys}")
        
    def create_q2d_dipole(self):
        pass
        return id_ansys

    def create_hfss_dipole(self):
        pass
        return id_ansys

        def set_analysis_type(self, analysis_type):
        """
        Cambia el tipo de análisis entre 'Q2D' y 'HFSS'.
        
        :param analysis_type: Tipo de análisis ('Q2D' o 'HFSS').
        """
        if analysis_type == "Q2D":
            self.type_ansys = "Q2D"
            # Aquí puedes realizar las configuraciones específicas para Q2D
            print("El tipo de análisis se ha configurado en Q2D.")
            
        elif analysis_type == "HFSS":
            self.type_ansys = "HFSS"
            # Aquí puedes realizar las configuraciones específicas para HFSS
            print("El tipo de análisis se ha configurado en HFSS.")
            
        else:
            raise ValueError("Tipo de análisis no reconocido. Usa 'Q2D' o 'HFSS'.")