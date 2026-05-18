
import pandas as pd
import matplotlib.pyplot as plt

# Lectura del dataset de ventas
df = pd.read_csv('datos/ventas.csv')

# Creación de columna de ventas totales
df['ventas_totales'] = df['cantidad'] * df['precio']

# Cálculo de indicadores básicos
ventas_totales = df['ventas_totales'].sum()

producto_mas_vendido = (
    df.groupby('producto')['cantidad']
    .sum()
    .idxmax()
)

ventas_por_mes = (
    df.groupby(df['fecha'].str[:7])['ventas_totales']
    .sum()
)

# Mostrar resultados por consola
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Generación del gráfico
ventas_por_mes.plot(kind='bar')

plt.title('Ventas por mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')

# Guardado del gráfico
plt.savefig('resultados/grafico_ventas.png')

# Guardado de resumen en archivo de texto
with open('resultados/resumen_ventas.txt', 'w') as archivo:
    archivo.write(f"Ventas totales: {ventas_totales}\n")
    archivo.write(f"Producto más vendido: {producto_mas_vendido}\n")
