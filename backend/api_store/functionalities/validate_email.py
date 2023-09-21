import re

def validar_correo(correo):
    # Patrón para validar el correo
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verificar si el correo cumple con el patrón
    if re.match(patron, correo):
        return True
    else:
        return False