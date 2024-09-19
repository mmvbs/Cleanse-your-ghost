from classes.objeto import Objeto
class Tumulos(Objeto):
    def __init__(self, largura, altura, tela):
        super().__init__(largura, altura, tela, "stone-1.png", 12, 900, 480, 100, 140)

    def load_images(self):
        super().load_images("stone-1.png", 100, 140)  

    def draw(self):
        super().draw()

    def update(self):
        super().update()
