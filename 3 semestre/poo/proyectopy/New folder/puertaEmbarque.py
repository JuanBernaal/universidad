class PuertaEmbarque:
    def __init__(self, nombre):
        self.identificacion = nombre
        self.disponibilidad = True

    def anunciarEmbarque(self, puerta):
        print(f"Anuncio de embarque en {self.identificacion} - Puerta {puerta}")
