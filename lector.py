# Herramienta para encontrar subsecuencias (lecturas) dentro de una secuencia de ADN
# incluso si contienen un solo error de nucleótido

def obtener_secuencia():
    """
    Devuelve una secuencia de referencia de ADN (gen ABO de Homo sapiens).
    Extraída de: http://www.ncbi.nlm.nih.gov/nuccore/LC068776.1
    """
    referencias = [
        'ggccgcctcc cgcgcccctc tgtcccctcc cgtgttcggc ctcgggaagt cggggcggcg',
        'ggcggcgcgg gccgggaggg gtcgcctcgg gctcaccccg ccccagggcc gccgggcgga',
        'aggcggaggc cgagaccaga cgcggagcca tggccgaggt gttgcggacg ctggccg',
    ]

    secuencia = ''.join(referencias)
    return secuencia.replace(' ', '')  # Quita los espacios


def construir_indice(secuencia, longitud_clave):
    """
    Crea un índice de subsecuencias de longitud fija (clave) para búsqueda rápida.
    :param secuencia: secuencia completa de ADN
    :param longitud_clave: largo de la subsecuencia a indexar
    :return: diccionario {subsecuencia: posicion}
    """
    indice = {}
    for i in range(len(secuencia) - longitud_clave + 1):
        fragmento = secuencia[i:i + longitud_clave]
        indice[fragmento] = i + 1  # usamos base 1
    return indice


def obtener_posicion(lectura, longitud_clave, indice):
    """
    Encuentra la posición de una lectura dentro de la secuencia usando el índice,
    permitiendo un posible error en una mitad de la lectura.
    :param lectura: subsecuencia a buscar (de largo 2*longitud_clave)
    :param longitud_clave: longitud de la clave usada en el índice
    :param indice: diccionario de subsecuencias
    :return: posición estimada (base 1)
    """
    # Dividimos la lectura en dos mitades
    parte1 = lectura[0:longitud_clave]
    parte2 = lectura[longitud_clave:2 * longitud_clave]

    # Buscamos la primera parte
    encontrada = indice.get(parte1, 0)
    if encontrada:
        return encontrada
    else:
        return indice.get(parte2, 0) - longitud_clave


def principal():
    """
    Ejecuta pruebas de búsqueda de lecturas en la secuencia de ADN,
    permitiendo un error por lectura.
    """
    longitud_clave = 7
    referencia = obtener_secuencia()
    indice = construir_indice(referencia, longitud_clave)

    # Pruebas con lecturas de 14 letras que podrían tener un error
    assert obtener_posicion('ccggcctcgggaag', longitud_clave, indice) == 36
    assert obtener_posicion('ttgcggacgctagc', longitud_clave, indice) == 162
    assert obtener_posicion('tcgggctccccccg', longitud_clave, indice) == 87
    assert obtener_posicion('ggggggaaggcgga', longitud_clave, indice) == 114
    assert obtener_posicion('tctgtccccccccg', longitud_clave, indice) == 19

    print("Todas las pruebas pasaron correctamente")


# Punto de entrada del script
if __name__ == "__main__":
    principal()
