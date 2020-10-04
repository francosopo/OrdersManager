
class DuplicatedValue(Exception):
    def __init__(self, nombre, apellido):
        super().__init__("{} {} ya existe".format(nombre, apellido))