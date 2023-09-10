import secrets
import string
import random

#función principal
def generar_contraseña_segura(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña



# Lista de palabras para crear contraseñas
palabras = ["manzana", "banana", "cereza", "delfín", "elefante", "flor", "gato", "helado", "iguana", "jirafa"]

# Función para generar una contraseña segura
def generar_contraseña_segura_recordable(longitud=4, palabras_lista=palabras):
    if longitud < 2:
        raise ValueError("La longitud mínima debe ser al menos 2 para hacer contraseñas seguras.")

    # Seleccionar palabras aleatorias
    palabras_elegidas = random.sample(palabras_lista, longitud - 1)

    # Agregar un número aleatorio al final de la contraseña
    numero_aleatorio = str(secrets.randbelow(100))
    palabras_elegidas.append(numero_aleatorio)

    # Mezclar las palabras elegidas
    random.shuffle(palabras_elegidas)

    # Formatear la contraseña como una sola cadena
    contraseña = ''.join(palabras_elegidas)

    return contraseña

# Invocación de la función e impresión
contraseña1 = generar_contraseña_segura_recordable()
print(contraseña1)

#invocación de la función e impresión
contraseña2 = generar_contraseña_segura()
print(contraseña2)
