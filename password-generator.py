import secrets
import string

def generar_contraseña_segura(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

contraseña = generar_contraseña_segura()
print(contraseña)
