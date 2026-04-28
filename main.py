class Transport:
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik

    def info(self):
        print(f"nomi: {self.nomi}")
        print(f"tezlik: {self.tezlik}")

class Mashina(Transport):
    def __init__(self, nomi, tezlik, yoqilgi):
        super().__init__(nomi, tezlik)
        self.yoqilgi = yoqilgi

    def info(self):
        super().info()
        print(f"yoqilgi: {self.yoqilgi}")

m = Mashina("Maluba", 120, "benzin")
m.info()
