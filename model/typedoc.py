from enum import Enum

class TypeDoc(str, Enum):
    CC = "Cedula de Ciudadania"
    TI = "Tarjeta de Identidad"
    RC = "Registro Civil"
    PAS = "Pasaporte"