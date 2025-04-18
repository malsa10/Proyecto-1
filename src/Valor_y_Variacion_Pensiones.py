# Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
df_pension_data = pd.read_csv('PensionMedia.csv')

# Eliminar la columna 'Unnamed: 1'
df_pension_data = df_pension_data.drop(columns=['Unnamed: 1'])

# Seleccionar solo las columnas 'Unnamed: 0' y 'Unnamed: 3'
df_pension_data = df_pension_data[['Unnamed: 0', 'Unnamed: 3']]

# Renombrar las columnas
df_pension_data = df_pension_data.rename(columns={'Unnamed: 0': 'Año', 'Unnamed: 3': 'Pension Media Mensual'})

# Convertir la columna 'Año' a tipo numérico, eliminando los valores no numéricos
df_pension_data['Año'] = pd.to_numeric(df_pension_data['Año'], errors='coerce')

# Eliminar filas con valores nulos en la columna 'Año'
df_pension_data = df_pension_data.dropna(subset=['Año'])

# Convertir la columna 'Año' a tipo entero
df_pension_data['Año'] = df_pension_data['Año'].astype(int)

# Restablecer el índice del DataFrame
df_pension_data = df_pension_data.reset_index(drop=True)

# Crear un DataFrame con las filas hasta la fila 13 incluida
df_pension_data_limited = df_pension_data.iloc[:12].reset_index(drop=True)

# Crear un nuevo DataFrame con las filas desde la fila 14 en adelante
df_variacion_pension = df_pension_data.iloc[12:].reset_index(drop=True)

# Renombrar las columnas del nuevo DataFrame
df_variacion_pension.columns = ['Año', 'Variación']


# Para df_pension_data_limited
df_pension_data_limited = df_pension_data_limited.sort_values('Pension Media Mensual', ascending=False).drop_duplicates(subset='Año', keep='first').reset_index(drop=True)

# Para df_variacion_pension
df_variacion_pension = df_variacion_pension.sort_values('Variación', ascending=False).drop_duplicates(subset='Año', keep='first').reset_index(drop=True)

# Ordenar df_pension_data_limited por la columna 'Año'
df_pension_data_limited = df_pension_data_limited.sort_values(by='Año', ascending=True).reset_index(drop=True)

# Ordenar df_variacion_pension por la columna 'Año'
df_variacion_pension = df_variacion_pension.sort_values(by='Año', ascending=True).reset_index(drop=True)

# Mostrar los DataFrames resultantes
print("DataFrame df_pension_data_limited sin años repetidos:")
print(df_pension_data_limited)

print("DataFrame df_variacion_pension sin años repetidos:")
print(df_variacion_pension)

# Guardar el DataFrame df_pension_data_limited en un archivo CSV
#df_pension_data_limited.to_csv("df_pension_data_limited.csv", sep=';', decimal='.', index=False, encoding='utf-8')

df_pension_data_limited.to_csv("df_pension_data_limited.csv", sep=';', decimal=',', index=False, encoding='utf-8')

# Guardar el DataFrame df_IPC en un archivo CSV
#df_variacion_pension.to_csv("df_variacion_pension.csv", sep=';', decimal='.', index=False, encoding='utf-8')

df_variacion_pension.to_csv("df_variacion_pension.csv", sep=';', decimal=',', index=False, encoding='utf-8')