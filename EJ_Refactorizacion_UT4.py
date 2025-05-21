from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class Receta(ABC):
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingredientes  # ingredientes
        self.pasos = pasos  # pasos

    @abstractmethod
    def mostrar(self):
        print(f"Receta vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas vegetarianas
class RecetaVegetariana(Receta):
    def mostrar(self):
        return super().mostrar()


# Clase para recetas no vegetarianas
class RecetaNoVegetariana(Receta):
    def mostrar(self):
        return super().mostrar()

# Clase con utilidades del restaurante
class Utilidades:
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for ingrediente in lista:
            print(f"* {ingrediente}")

    @staticmethod
    def crearReceta():
        ingredientes = []
        pasos = []
        nombre = input("Dame el nombre de la receta")
        cantidadIngredientes = int(input("Cuantos ingedientes quieres "))
        for ingrediente in range(cantidadIngredientes):
            ingrediente = input("Dime el nombre del ingrediente ")
            ingredientes.append(ingrediente)

        cantidadDePasos = int(input("Cuantos pasos vas a hacer "))
        for paso in range(cantidadDePasos):
            paso = input("Dime el paso ")
            pasos.append(paso)
       
        tipo = input("Que receta vas a hacer ")
        if tipo.lower() == "vegetariana":
            return RecetaVegetariana(nombre, ingredientes, pasos)
        
        elif tipo.lower()== "no vegetariana":
            return RecetaNoVegetariana(nombre, ingredientes, pasos)

# Función principal
def principal():
    recetasCreadas = []
    for recetaCreada in range(2):
       receta = Utilidades.crearReceta()
       recetasCreadas.append(receta)
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    Utilidades.imprimir_receta(recetasCreadas[0])
    Utilidades.imprimir_receta(recetasCreadas[1])

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ingrediente in recetasCreadas[0]:
        print(f"* {ingrediente}")
    
    print("Ingredientes de Pollo al horno:")
    for ingrediente in recetasCreadas[1]:
        print(f"* {ingrediente}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
