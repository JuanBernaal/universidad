from view import View

class Controller:
    def __init__(self, view, aeropuerto):
        self.view = view
        self.aeropuerto = aeropuerto

    def ejecutar(self):
        option = self.view.mainMenu()