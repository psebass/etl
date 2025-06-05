import pandas as pd
import unicodedata


def limpiar_datos(df):
    # Eliminar columnas completamente vacías
    df = df.dropna(how='all')

    # Eliminar espacios en los nombres de columnas
    df.columns = df.columns.str.strip()

    # Reemplazar acentos en los nombres de columnas
    df.columns = [
        ''.join(c for c in unicodedata.normalize('NFD', col) 
                if unicodedata.category(c) != 'Mn') for col in df.columns]

    # Convertir nombres de columnas a minúsculas
    df.columns = [col.lower() for col in df.columns]

    # Eliminar filas duplicadas
    df = df.drop_duplicates()

    # Rellenar nulos
    df = df.fillna('-')

    return df
