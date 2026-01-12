# RETO 06 — VERDE OSCURO

Proyecto de análisis y modelado de cancelaciones en Líbere.

============================================================

## DESCRIPCIÓN DEL PROYECTO

Este proyecto analiza la problemática de las cancelaciones en Líbere mediante
el uso de datos internos y técnicas de análisis de datos, visualización,
segmentación de clientes y modelos predictivos.

El objetivo es comprender los patrones de comportamiento de los clientes,
identificar segmentos relevantes y proponer mejoras basadas en los resultados
obtenidos.

============================================================

## NOTA SOBRE LOS DATOS

El archivo de datos original proporcionado por Líbere se denomina
`cancellation_data_for_mondragon_unibertsitatea_2024.csv`.

Con el objetivo de facilitar la lectura, el trabajo con los datos y la
reutilización del proyecto, dicho archivo ha sido renombrado a
`cancellation_data.csv`, manteniendo íntegramente su contenido original.

## ESTRUCTURA DEL PROYECTO
------------------------------------------------------------
```
RETO_06_VerdeOSCURO/
│
├── 01-Limpieza.ipynb
├── 02-Analisis_Exploratorio.ipynb
├── 03-webscrapping.ipynb
├── 04-api.ipynb
├── 05-Dummies_Clustering.ipynb
├── 06-Clustering.ipynb
├── 07-Modelado.ipynb
├── 08-Modelado_PCA.ipynb
├── 09-ElasticSearch_Indexacion.ipynb
│
├── entorno_VERDEOSCURO_RET06.yml
├── .gitignore
├── RETO_06_VerdeOSCURO.code-workspace
├── README.md
│
├── packages/
│   ├── EDA/
│   └── Preprocesamiento/
│       └── funciones_limpieza.py
│
├── Datos/
│   ├── Originales/
│   └── Transformados/
│
├── Graficos/
│
├── config_files/
│   └── api_config.json

```

============================================================

## ORDEN DE EJECUCIÓN DE LOS NOTEBOOKS
------------------------------------------------------------

Para garantizar la correcta reproducción del análisis y del flujo de datos,
los notebooks deben ejecutarse en el siguiente orden:

1) 01-Limpieza.ipynb  
2) 02-Analisis_Exploratorio.ipynb  
3) 03-webscrapping.ipynb  
4) 04-api.ipynb  
5) 05-Dummies_Clustering.ipynb  
6) 06-Clustering.ipynb  
7) 07-Modelado.ipynb  
8) 08-Modelado_PCA.ipynb  
9) 09-ElasticSearch_Indexacion.ipynb  

============================================================

## CONTENIDO DE LA CARPETA `packages`
------------------------------------------------------------

La carpeta `packages` contiene módulos reutilizables desarrollados para el
tratamiento y análisis de los datos.

En particular, dentro de `packages/Preprocesamiento` se encuentra el archivo
`funciones_limpieza.py`, que incluye funciones auxiliares para la limpieza
y preparación de los datos.

Entre ellas se encuentra la función `convertir_fechas`, utilizada para
convertir una o varias columnas de un DataFrame a formato `datetime`,
gestionando automáticamente distintos formatos de fecha y valores erróneos.

============================================================

## CONFIGURACIÓN DE LA API
------------------------------------------------------------

La carpeta `config_files` contiene el archivo `api_config.json`, donde se
almacena la clave necesaria para el acceso a la API utilizada en el proyecto.

Este enfoque permite separar la configuración sensible del código fuente
y facilita la reutilización del proyecto sin modificar los notebooks.

============================================================


## INSTRUCCIONES PARA INSTALAR EL ENTORNO (reto06_VerdeOscuro)
------------------------------------------------------------
1) Crear el entorno con Conda

Abrir Anaconda Prompt, situarse en la carpeta del proyecto
(donde está el archivo entorno_VERDEOSCURO_RET06.yml) y ejecutar:

conda env create -f entorno_VERDEOSCURO_RET06.yml

Cuando pregunte:
Proceed ([y]/n)?

Escribir: y

------------------------------------------------------------

2) Seleccionar el intérprete en VS Code

- Abrir el proyecto (preferiblemente usando el archivo .code-workspace).
- Abajo a la derecha: “Seleccionar intérprete”.
- Elegir: Python (reto06_VerdeOscuro).

============================================================

## AUTORÍA
------------------------------------------------------------
Proyecto desarrollado por el Grupo Verde Oscuro  
Reto 06 
