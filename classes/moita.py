from classes.objeto import Objeto
class Moita(Objeto):
    def __init__(self, largura, altura, tela):
        super().__init__(largura, altura, tela, "bush-large.png", 12, 400, 500, 152, 130)

    def load_images(self):
        super().load_images("bush-large.png", 152, 130)  

    def draw(self):
        super().draw()

    def update(self):
        super().update()
