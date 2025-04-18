import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_Hipotecas = pd.read_csv('Hipotecas_.csv', sep=';')


# Eliminar las filas desde el índice 0 hasta el 5 (incluidos)
df_Hipotecas = df_Hipotecas.drop(range(0, 6)).reset_index(drop=True)

# Crear las columnas DATE y VALOR
df_Hipotecas['DATE'] = df_Hipotecas.iloc[:, 0].apply(lambda x: str(x).split(',')[0])  # Antes de la primera coma
df_Hipotecas['VALOR'] = df_Hipotecas.iloc[:, 0].apply(lambda x: str(x).split(',')[1] if ',' in str(x) else None)  # Entre la primera y segunda coma

# Eliminar la primera columna por índice
df_Hipotecas = df_Hipotecas.drop(df_Hipotecas.columns[0], axis=1)

# Eliminar la fila con índice 0
df_Hipotecas = df_Hipotecas.drop(0).reset_index(drop=True)

# Reemplazar la letra 'M' por '/' en la columna 'DATE'
df_Hipotecas['DATE'] = df_Hipotecas['DATE'].str.replace('M', '/', regex=False)

# Extraer el año de la columna 'DATE' y crear una nueva columna 'AÑO'
df_Hipotecas['AÑO'] = df_Hipotecas['DATE'].str.extract(r'(\d{4})')

# Filtrar las filas que tengan valores no numéricos en la columna 'AÑO'
df_Hipotecas = df_Hipotecas[df_Hipotecas['AÑO'].notna()].reset_index(drop=True)

# Convertir la columna 'AÑO' a tipo entero (opcional, si se requiere)
df_Hipotecas['AÑO'] = df_Hipotecas['AÑO'].astype(int)

# Mostrar el DataFrame resultante
print(df_Hipotecas)

# Mostrar el DataFrame resultante
print(df_Hipotecas.head())


# Guardar el DataFrame df_Hipotecas en un archivo CSV
df_Hipotecas.to_csv("df_Hipotecas.csv", sep=';', decimal=',', index=False, encoding='utf-8')

# Confirmación
print("El DataFrame df_Hipotecas se ha guardado como 'df_Hipotecas.csv'.")