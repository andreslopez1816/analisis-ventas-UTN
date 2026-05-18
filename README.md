# Análisis de Ventas - Trabajo Práctico UTN

## Descripción del Proyecto

Este proyecto fue desarrollado para la materia Organización Empresarial de la Tecnicatura Universitaria en Programación de la Universidad Tecnológica Nacional (UTN).

El trabajo práctico tiene como objetivo aplicar herramientas de gestión colaborativa y control de versiones mediante el uso de Git, GitHub, Jira y Google Colab, simulando el flujo de trabajo de una célula ágil de desarrollo.

El escenario seleccionado corresponde al análisis de ventas de una pequeña empresa.

---

## Integrante

- Carlos Andrés López

---

## Tecnologías Utilizadas

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Jira
- Google Colab

---

## Estructura del Proyecto

```text
analisis-ventas-UTN/
│
├── datos/
│   └── ventas.csv
│
├── scripts/
│   └── analisis_ventas.py
│
├── resultados/
│   ├── grafico_ventas.png
│   └── resumen_ventas.txt
│
├── README.md
└── .gitignore
```

---

## Funcionalidades Implementadas

El script desarrollado permite:

- Importar datos de ventas desde un archivo CSV.
- Calcular ventas totales.
- Identificar el producto más vendido.
- Generar un gráfico de ventas por mes.
- Exportar resultados automáticamente.

---

## Ejecución del Proyecto

Ejecutar el siguiente comando desde la raíz del proyecto:

```bash
python scripts/analisis_ventas.py
```

---

## Resultados Generados

El proyecto genera automáticamente:

- Un gráfico de ventas:
  - `resultados/grafico_ventas.png`

- Un resumen del análisis:
  - `resultados/resumen_ventas.txt`

---

## Gestión y Trazabilidad

Durante el desarrollo del proyecto se utilizaron:

- Issues en Jira para planificación y seguimiento.
- Conventional Commits con trazabilidad mediante IDs.
- Branches para desarrollo separado.
- Pull Requests y revisión técnica (Peer Review).

Ejemplos de commits realizados:

- `KAN-5: Crear estructura inicial del proyecto`
- `KAN-6: Agregar análisis de ventas y generación de resultados`

---

## Autor

Trabajo desarrollado para la materia Organización Empresarial  
Tecnicatura Universitaria en Programación - UTN
