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

## INSTRUCCIONES PARA INSTALAR EL ENTORNO (reto06_VerdeOscuro)
------------------------------------------------------------

1) Requisitos previos
- Tener Anaconda o Miniconda instalado.
- Tener Git y Visual Studio Code instalados.
- Tener el archivo entorno_VERDEOSCURO_RET06.yml dentro de la carpeta del proyecto.

------------------------------------------------------------

2) Crear el entorno con Conda

Abrir Anaconda Prompt, situarse en la carpeta del proyecto
(donde está el archivo entorno_VERDEOSCURO_RET06.yml) y ejecutar:

conda env create -f entorno_VERDEOSCURO_RET06.yml

Cuando pregunte:
Proceed ([y]/n)?

Escribir: y

------------------------------------------------------------

3) Activar el entorno

conda activate reto06_VerdeOscuro

Debe aparecer:
(reto06_VerdeOscuro)

------------------------------------------------------------

4) Crear el kernel para VS Code / Jupyter

Ejecutar:

python -m ipykernel install --user --name reto06_VerdeOscuro --display-name "Python (reto06_VerdeOscuro)"

------------------------------------------------------------

5) Seleccionar el intérprete en VS Code

- Abrir el proyecto (preferiblemente usando el archivo .code-workspace).
- Abajo a la derecha: “Seleccionar intérprete”.
- Elegir: Python (reto06_VerdeOscuro).

------------------------------------------------------------

6) Listo

El entorno ya está configurado y se puede trabajar en el proyecto.

============================================================

## AUTORÍA
------------------------------------------------------------
Proyecto desarrollado por el Grupo Verde Oscuro  
Reto 06 