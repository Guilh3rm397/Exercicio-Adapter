from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def tocar(self, arquivo):
        pass


class PlayerMP3(Player):
    def tocar(self, arquivo):
        print("Tocando MP3:", arquivo)


class PlayerMP4:
    def abrir_mp4(self, arquivo):
        print("Tocando MP4:", arquivo)


class PlayerVLC:
    def abrir_vlc(self, arquivo):
        print("Tocando VLC:", arquivo)


class AdaptadorMP4(Player):
    def __init__(self):
        self.player = PlayerMP4()

    def tocar(self, arquivo):
        self.player.abrir_mp4(arquivo)


class AdaptadorVLC(Player):
    def __init__(self):
        self.player = PlayerVLC()

    def tocar(self, arquivo):
        self.player.abrir_vlc(arquivo)


class Plataforma:
    def __init__(self, player):
        self.player = player

    def tocar(self, arquivo):
        self.player.tocar(arquivo)


class Principal:
    def executar(self):
        Plataforma(PlayerMP3()).tocar("samba.mp3")
        Plataforma(AdaptadorMP4()).tocar("clipe.mp4")
        Plataforma(AdaptadorVLC()).tocar("show.vlc")


if __name__ == "__main__":
    Principal().executar()
