import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV
df_VEGI = pd.read_csv('VEGI_historico.csv')

# Eliminar las tres últimas columnas del DataFrame
df_VEGI = df_VEGI.iloc[:, :-3]


# Renombrar las columnas
df_VEGI.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Eliminar las filas 0 y 1
df_VEGI = df_VEGI.drop([0, 1]).reset_index(drop=True)

# Convertir la columna 'Date' al formato datetime
df_VEGI['Date'] = pd.to_datetime(df_VEGI['Date'])


# Función para dividir valores mayores a 800 entre 10
def adjust_values(value):
    if value > 650:
        value /= 10
    return value

# Función para limpiar y escalar los valores numéricos
def clean_and_scale(value):
    # Eliminar separadores de miles (puntos y comas)
    value = str(value).replace('.', '').replace(',', '')
    # Convertir a float
    value = float(value)
    # Escalar el valor para que tenga solo tres números enteros
    while value >= 1000:  # Ajustar la escala si el número tiene más de tres dígitos enteros
        value /= 10
    return round(value, 2)  # Redondear a 2 decimales

# Aplicar la función a las columnas numéricas
for col in ['Close', 'High', 'Low', 'Open']:
    df_VEGI[col] = df_VEGI[col].apply(clean_and_scale)

    # Aplicar la función a las columnas numéricas después de limpiar los datos
for col in ['Close', 'High', 'Low', 'Open']:
    df_VEGI[col] = df_VEGI[col].apply(adjust_values)

# Mostrar el DataFrame resultante
print(df_VEGI)

# Guardar el DataFrame df_IPC en un archivo CSV
#df_VEGI.to_csv("df_VEGI.csv", sep=';', decimal='.', index=False, encoding='utf-8')

df_VEGI.to_csv("df_VEGI.csv", sep=';', decimal=',', index=False, encoding='utf-8')

# Confirmación
print("El DataFrame df_VEGI se ha guardado como 'df_VEGI.csv'.")

# Graficar el precio de cierre (Close) a lo largo del tiempo
plt.figure(figsize=(12, 6))
plt.plot(df_VEGI['Date'], df_VEGI['Close'], label='Close Price', color='blue')
plt.title('S&P 500 - Precio de Cierre Ajustado')
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()