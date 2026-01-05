import pandas as pd

def read_data(filename):
    return pd.read_csv(filename, index_col = [0])

def remove_column(df, colnames):
    return df.drop(columns=colnames)

def remove_rows_with_nas(df, colnames):
    return df[df[colnames].notna()]

def save_clean_data(df, file):
    df.to_csv(file)
    return None
def convertir_fechas(df, columnas):
    """
    Convierte una o varias columnas de un DataFrame a datetime.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    columnas : str o list
        Nombre de la columna o lista de columnas a convertir.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con las columnas convertidas a datetime.
    """

    # Si se pasa una sola columna como string, la convertimos en lista
    if isinstance(columnas, str):
        columnas = [columnas]

    for col in columnas:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], format="mixed", errors="coerce")

    return df