from abc import ABC, abstractmethod


class Renderizador(ABC):
    @abstractmethod
    def desenhar_circulo(self, raio):
        pass

    @abstractmethod
    def desenhar_quadrado(self, lado):
        pass


class RenderizadorVetorial(Renderizador):
    def desenhar_circulo(self, raio):
        print(f"[Vetorial] Círculo com raio {raio} desenhado por curvas")

    def desenhar_quadrado(self, lado):
        print(f"[Vetorial] Quadrado com lado {lado} desenhado por linhas")


class RenderizadorRaster(Renderizador):
    def desenhar_circulo(self, raio):
        print(f"[Raster] Círculo com raio {raio} desenhado por pixels")

    def desenhar_quadrado(self, lado):
        print(f"[Raster] Quadrado com lado {lado} desenhado por pixels")


class Forma(ABC):
    def __init__(self, renderizador):
        self.renderizador = renderizador  

    @abstractmethod
    def desenhar(self):
        pass


class Circulo(Forma):
    def __init__(self, renderizador, raio):
        super().__init__(renderizador)
        self.raio = raio

    def desenhar(self):
        self.renderizador.desenhar_circulo(self.raio)


class Quadrado(Forma):
    def __init__(self, renderizador, lado):
        super().__init__(renderizador)
        self.lado = lado

    def desenhar(self):
        self.renderizador.desenhar_quadrado(self.lado)


class Principal:
    def executar(self):
        vetorial = RenderizadorVetorial()
        raster = RenderizadorRaster()

        formas = [
            Circulo(vetorial, 5),
            Circulo(raster, 5),
            Quadrado(vetorial, 4),
            Quadrado(raster, 4),
        ]
        for forma in formas:
            forma.desenhar()


if __name__ == "__main__":
    Principal().executar()