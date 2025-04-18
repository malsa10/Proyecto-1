import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer el CSV original
df_IPC = pd.read_csv('IPC.csv', sep=';')

# 2. Seleccionar y renombrar columnas
df_IPC = df_IPC.iloc[:, -2:]
df_IPC.columns = ['Date', 'Variacion_IPC']

# 3. Limpiar y convertir formatos
#    - Reemplazar 'M' por '/' y pasar a datetime
df_IPC['Date'] = df_IPC['Date'].str.replace('M', '/', regex=False)
df_IPC['Date'] = pd.to_datetime(df_IPC['Date'], dayfirst=True)  # asumiendo formato día/mes/año

#    - Asegurarnos de que 'Variacion_IPC' sea numérico
#      (p.ej. si viene con coma decimal)
df_IPC['Variacion_IPC'] = (
    df_IPC['Variacion_IPC']
    .astype(str)
    .str.replace(',', '.', regex=False)
    .astype(float)
)

# 4. Ordenar por fecha
df_IPC = df_IPC.sort_values('Date').reset_index(drop=True)

# 5. Calcular la suma acumulada
df_IPC['IPC_suma'] = df_IPC['Variacion_IPC'].cumsum()

# 6. Verificar resultados
print(df_IPC.head())


# 7. Guardar el CSV con la nueva columna
# Guardar el DataFrame en un archivo CSV
df_IPC.to_csv("df_IPC_filtrado_con_suma.csv", sep=';', decimal=',', index=False, encoding='utf-8')
print("Guardado en 'df_IPC_filtrado_con_suma.csv'")

# 8. Graficar
plt.figure(figsize=(10, 6))
plt.plot(df_IPC['Date'], df_IPC['IPC_suma'], marker='o')
plt.title('Evolución acumulada de la Variación IPC')
plt.xlabel('Fecha')
plt.ylabel('Suma acumulada de Variación IPC')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()