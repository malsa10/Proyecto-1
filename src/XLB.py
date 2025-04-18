import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV
df_XLB = pd.read_csv('XLB_historico.csv')

# Eliminar las tres últimas columnas del DataFrame
df_XLB = df_XLB.iloc[:, :-3]

# Renombrar las columnas
df_XLB.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Eliminar las filas 0 y 1
df_XLB = df_XLB.drop([0, 1]).reset_index(drop=True)

# Convertir la columna 'Date' a datetime forzando el uso de UTC
df_XLB['Date'] = pd.to_datetime(df_XLB['Date'], errors='coerce', utc=True)

# Convertir los datetimes *tz-aware* a datetimes *naive* (sin zona horaria)
df_XLB['Date'] = df_XLB['Date'].dt.tz_convert(None)

# Función para limpiar y escalar los valores numéricos
def clean_and_scale(value):
    # Eliminar separadores de miles (puntos y comas)
    value = str(value).replace('.', '').replace(',', '')
    # Convertir a float
    value = float(value)
    # Escalar el valor para que tenga solo tres números enteros
    while value >= 1000:  
        value /= 10
    # Si el valor escalado es menor a 100, reducirlo según tu lógica
    if value < 100:
        value /= 10
    return round(value, 2)

# Aplicar la función a las columnas numéricas
for col in ['Close', 'High', 'Low', 'Open']:
    df_XLB[col] = df_XLB[col].apply(clean_and_scale)

# Condición final:
# Para filas anteriores al año 2016, si en las columnas Open, High, Low o Close el valor es superior a 250, se divide entre 10.
mask = df_XLB['Date'] < pd.to_datetime("2004-01-01")
for col in ['Open', 'High', 'Low', 'Close']:
    df_XLB.loc[mask & (df_XLB[col] > 200), col] = df_XLB.loc[mask & (df_XLB[col] > 200), col] / 10

# Verificar la conversión de 'Date'
print("Tipo de 'Date':", df_XLB['Date'].dtype)
print(df_XLB['Date'].head())

# Guardar el DataFrame en un archivo CSV
df_XLB.to_csv("df_XLB.csv", sep=';', decimal=',', index=False, encoding='utf-8')
print("El DataFrame df_XLB se ha guardado como 'df_XLB.csv'.")

# Graficar el precio de cierre (Close) a lo largo del tiempo
plt.figure(figsize=(12, 6))
plt.plot(df_XLB['Date'], df_XLB['Close'], label='Close Price', color='blue')
plt.title('df_XLB - Precio de Cierre Ajustado')
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()