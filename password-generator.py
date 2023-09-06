import secrets
import string

def generar_contraseņa_segura(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseņa = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseņa

contraseņa = generar_contraseņa_segura()
print(contraseņa)
