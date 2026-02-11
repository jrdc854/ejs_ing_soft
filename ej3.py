def analizar_titulares(lista):
    palabras_relevantes = set()

    for titular in lista:
        palabras = titular.split()
        for palabra in palabras:
            palabra_limpia = palabra.strip(".,;:¡!¿?()\"'").lower()

            if len(palabra_limpia) > 6:
                palabras_relevantes.add(palabra_limpia)

    palabras_ordenadas = sorted(palabras_relevantes)
    return palabras_ordenadas, len(palabras_ordenadas)

resultado, numero = analizar_titulares([
    "El presidente anuncia nuevas medidas económicas",
    "El ministro de cultura visita la exposición de arte",
    "El alcalde inaugura un nuevo parque en la ciudad"
])
print(f'Palabras relevantes: {resultado}\ntotal de palabras: {numero}')