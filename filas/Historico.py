from datetime import datetime

class Historico:
    def __init__(self, pagina):
        self.pagina = pagina
        self.horario = datetime.now()

    def __str__(self):
        return str(f"{self.pagina} - {self.horario}")