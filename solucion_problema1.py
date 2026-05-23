# ---------------------------------------------------------
# Nombre del Estudiante: Laura Sofia Matallana Reina
# Grupo: 213022
# Programa Académico: Ingeniería de Sistemas
# Código Fuente: Autoría propia
# ---------------------------------------------------------

def clasificar_compromiso(duracion, clics):
    """
    Módulo (función) que calcula la clasificación de compromiso 
    basándose en la duración de la sesión y la cantidad de clics [2].
    """
    # Lógica de Negocio:
    # Clasificar como "Alto" si Duración > 180s y Clics > 8 [2].
    if duracion > 180 and clics > 8:
        return "Alto"
    
    # Clasificar como "Bajo" si Duración < 60s o Clics < 3 [2].
    elif duracion < 60 or clics < 3:
        return "Bajo"
    
    # Clasificar como "Medio" en todos los demás casos [2].
    else:
        return "Medio"

def generar_informe_clientes():
    """
    Función principal que gestiona la matriz de datos y genera el reporte final [5].
    """
    # Requisito: Una matriz con al menos 5 filas de datos [2].
    # Formato de la matriz: [ID Cliente, Duración (segundos), Eventos Clics] [1].
    matriz_sesiones = [
        [6],  # Clasificación esperada: Alto
        [7, 8],    # Clasificación esperada: Bajo (Duración < 60s)
        [2, 9],   # Clasificación esperada: Bajo (Clics < 3)
        [10, 11],   # Clasificación esperada: Medio
        [12, 13]   # Clasificación esperada: Alto
    ]

    print("============================================")
    print("      INFORME DE COMPROMISO DE CLIENTES     ")
    print("============================================")
    print(f"{'ID Cliente':<15} | {'Clasificación':<15}")
    print("-" * 40)

    # Recorrido de la matriz para procesar cada sesión [3]
    for sesion in matriz_sesiones:
        id_cliente = sesion
        duracion = sesion[1]
        clics = sesion[2]
        
        # Llamada al módulo de clasificación
        resultado = clasificar_compromiso(duracion, clics)
        
        # Salida: Generar informe listando ID y clasificación [5]
        print(f"{id_cliente:<15} | {resultado:<15}")

    print("============================================")

# Punto de entrada del programa
if __name__ == "__main__":
    generar_informe_clientes()