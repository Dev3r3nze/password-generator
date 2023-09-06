import secrets
import string

def generar_contrase�a_segura(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrase�a = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrase�a

contrase�a = generar_contrase�a_segura()
print(contrase�a)
