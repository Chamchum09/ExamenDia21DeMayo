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
    def crearReceta(tipo):
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
       
        if tipo.lower() == "vegetariana":
            return RecetaVegetariana(nombre, ingredientes, pasos)
        
        elif tipo.lower()== "no vegetariana":
            return RecetaNoVegetariana(nombre, ingredientes, pasos)

# Función principal
def principal():
    #GUARDAR RECETAs
    listaDeRecetas = []

    #CREAR RECETAS
    for _ in range(2):
        tipo = input("Dime el tipo de receta que quieres crear ")
        receta = Utilidades.crearReceta(tipo)
        listaDeRecetas.append(receta)
    
    #MOSTRAR RECETAS
    print("== Mostrar recetas ==")
    for recta in listaDeRecetas:
        Utilidades.imprimir_receta(receta)

    #MOSTRAR INGREDIENTES

    for receta in listaDeRecetas:
        Utilidades.mostrar_lista_ingredientes(receta.ingredientes)

# Ejecutar el programa
if __name__ == "__main__":
    principal()
