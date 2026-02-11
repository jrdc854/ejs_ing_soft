# gestión de inventario de una librería

inventario = {
    "El Quijote": 7,
    "Don Juan Tenorio": 5,
    "La Celestina": 0
}

def añadir_libro(inventario, titulo):
    if titulo in inventario:
        return f'{titulo} ya está en el inventario, modifica el número de ejemplares'
    inventario[titulo] = 1
    return inventario

def actualizar_existencias(inventario, titulo , numero):
    if titulo in inventario:
            inventario[titulo] += numero
            return inventario
    
    return f'{titulo} no se encuentra en el inventario, añade el titulo'


def promedio_ejemplares(inventario):
    if len(inventario) > 0:
        promedio = sum(inventario.values()) / len(inventario)
        return promedio
    else:
        print("No hay libros en el inventario")
        return 0
    
def mostrar_resumen(inventario):
    if len(inventario) == 0:
        print("No hay libros en el inventario.")
        return 
    
    # Calcular promedio
    promedio = sum(inventario.values()) / len(inventario)
    print(f"Promedio de ejemplares por libro: {promedio:.2f}")
    
    # Libros con más ejemplares que el promedio
    print("\nLibros con más ejemplares que el promedio:")
    for titulo, cantidad in inventario.items():
        if cantidad > promedio:
            print(f"- {titulo} ({cantidad} ejemplares)")
    
    # Advertencia para libros con 0 ejemplares
    for titulo, cantidad in inventario.items():
        if cantidad == 0:
            print(f"⚠ Advertencia: '{titulo}' no tiene ejemplares disponibles.")


añadir_libro(inventario, "El Lazarillo de Tormes")
actualizar_existencias(inventario, "El Quijote", 8)
print(inventario) # Inventario actualizado

promedio_ejemplares(inventario)
mostrar_resumen(inventario)