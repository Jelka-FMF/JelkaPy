import jelka_validator.datawriter as dw

class Sphere:

    def __init__(self, radius):
        self.radius = radius
        inst = dw.DataWriter()
        inst.write_data([(255,0,255)])
    