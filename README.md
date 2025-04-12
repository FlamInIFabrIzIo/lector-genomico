# Lector Genómico

Lector Genómico es una herramienta diseñada para localizar subsecuencias específicas dentro de una secuencia de ADN, incluso si contienen un único error de nucleótido. Este proyecto implementa un algoritmo eficiente que utiliza un índice de subsecuencias para realizar búsquedas rápidas y tolerantes a errores.

## Características

- **Búsqueda tolerante a errores**: Permite localizar subsecuencias incluso si tienen un error en una de sus mitades.
- **Construcción de índices**: Crea un índice basado en subsecuencias de longitud fija para optimizar las búsquedas.
- **Pruebas integradas**: Incluye pruebas automatizadas para verificar el correcto funcionamiento del algoritmo.

## Cómo funciona

1. **Secuencia de referencia**: El programa utiliza una secuencia de ADN de referencia (gen ABO de Homo sapiens) extraída de [NCBI](http://www.ncbi.nlm.nih.gov/nuccore/LC068776.1).
2. **Construcción del índice**: Se genera un índice de subsecuencias de longitud fija (clave) para facilitar la búsqueda.
3. **Búsqueda de lecturas**: Se localizan subsecuencias de longitud doble a la clave, permitiendo un error en una de sus mitades.

