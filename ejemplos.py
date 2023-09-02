class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("La edad no puede ser negativa")

# Crear una instancia de Persona
persona = Persona("Juan", 25)

# Acceder a la propiedad nombre
print(persona.nombre)  # Salida: Juan

# Modificar la propiedad nombre
persona.nombre = "Pedro"
print(persona.nombre)  # Salida: Pedro

# Acceder a la propiedad edad
print(persona.edad)  # Salida: 25

# Intentar asignar una edad negativa (generará un mensaje de error)
persona.edad = -10  # Salida: La edad no puede ser negativa
