class Controller:
    def __init__(self, model, view, aeropuerto):
        self.model = model
        self.view = view
        self.aeropuerto = aeropuerto

    def ejecutar(self):
        while True:
            opcion = self.view.obtenerOpcion()

            if opcion == 1:
                tmp = None  ##### CAMBIAR AQUI!!!, se necesita que cree un vuelo a traves del VIEW y luego eso lo recibe el controller
                self.aeropuerto.agregarDestino(tmp)

            elif opcion == 2:
                self.agregarNaves(self.aeropuerto)
