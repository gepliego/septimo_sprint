# septimo_sprint
Sprint siete de TripleTen

# Proyecto de Análisis Exploratorio de Datos: Mercado de Vehículos

El proyecto consistio en el desarrollo de una aplicación web interactiva diseñada para analizar un conjunto de datos del mercado de anuncios de venta de vehículos en los Estados Unidos. A través de este proyecto, se realiza un análisis exploratorio de datos (EDA) permitiendo visualizar tendencias y relaciones entre variables clave como el precio, el kilometraje y el tipo de vehículo.

## Objetivo del Proyecto
Más allá del análisis de datos, el propósito fundamental de este trabajo fue proporcionar un entorno real para **practicar tareas habituales de ingeniería de software**. Esto incluye:
*   Configuración y gestión de entornos virtuales.
*   Control de versiones utilizando **Git** y **GitHub**.
*   Desarrollo de una interfaz de usuario funcional con **Streamlit**.
*   Despliegue continuo en plataformas en la nube (**Render**).
*   Escritura de código limpio y documentado siguiendo estándares de la industria.

## Tecnologías Utilizadas
*   **Python**: Lenguaje principal de desarrollo.
*   **Pandas**: Manipulación y limpieza del conjunto de datos `vehicles_us.csv`.
*   **Plotly**: Creación de gráficos interactivos (Histogramas y Gráficos de Dispersión).
*   **Streamlit**: Framework para la creación del dashboard web.
*   **Render**: Servicio de hosting para el despliegue de la aplicación.
*   **GitHub**: Repositorio y control de versiones.

## Instrucciones de Funcionamiento y Uso

### Ejecución Local
Si deseas replicar este trabajo en tu máquina local, sigue estos pasos:

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/nombre-del-repositorio.git
    cd nombre-del-repositorio
    ```

2.  **Crear y activar un entorno virtual** (macOS/Linux):
    ```bash
    python3 -m venv vehicles_env
    source vehicles_env/bin/activate
    ```

3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Lanzar la aplicación**:
    ```bash
    streamlit run app.py
    ```

### Uso de la Aplicación
Una vez abierta la aplicación en el navegador:
*   **Histograma**: Haz clic en el botón "Construir histograma" para visualizar la distribución de la columna de kilometraje (`odometer`).
*   **Gráfico de Dispersión**: Haz clic en el botón "Construir gráfico de dispersión" para analizar la relación entre el precio (`price`) y el kilometraje de los vehículos.

## Despliegue
Este proyecto ha sido desplegado de manera profesional para que cualquier usuario pueda acceder a él sin instalar código:

1.  **GitHub**: El código fuente se encuentra alojado en un repositorio público, lo que facilita la colaboración y el seguimiento de cambios.
2.  **Render**: Se vinculó el repositorio de GitHub a la plataforma Render. Cada vez que se realiza un *push* a la rama principal, la aplicación se actualiza automáticamente (CD - Despliegue Continuo).

**Puedes ver la aplicación en vivo aquí:** [Enlace a tu URL de Render]

---

### Notas de replicación
Para facilitar que otros repliquen el trabajo, el archivo `requirements.txt` incluye todas las versiones específicas de las librerías utilizadas, y el archivo `.gitignore` asegura que los archivos innecesarios (como el entorno virtual) no ensucien el repositorio.
