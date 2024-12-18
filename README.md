# Reto Soluas | Aplicativo SoluDash

## Problemática

Actualmente, la empresa Soluas enfrenta dificultades en la presentación mensual del informe de los
KPI’s del contrato con la Secretaría de Hacienda del municipio de Itagüí, ya que este informe se
entrega en un formato poco amigable y sin dinamismo, lo que complica la comprensión del avance de
las actividades por parte del cliente principal. Además, la estructura actual limita a los usuarios
internos, quienes carecen de una herramienta ágil para consultar y actualizar la información
eficientemente. La implementación de una base de datos dinámica permitiría estructurar los datos
de manera más accesible para el equipo interno y ofrecer una presentación visual e interactiva para
el cliente, optimizando la comunicación y el seguimiento de los indicadores de desempeño del
contrato.

## Alcance actual

Se creará un dashboard para consulta, actualización y generación de informes de los datos requeridos 
por el cliente, al cual se podrá acceder por medio de login en el cual se implementará controles de 
seguridad JWT. Además, una base de datos relacional para almacenamiento y mejor estructuración de los 
datos, el backend en python, y las respectivas API’s para interacción del dashboard.


## Stack tecnológico del Backend

### Arquitectura

Para éste aplicativo, se utilizó la arquitectura REST API.

### Tecnologías y herramientas

- [Python](https://www.python.org/): lenguaje de programación de alto nivel.
- [FastAPI](https://fastapi.tiangolo.com/): framework de Python que permite construir APIs de manera rápida y eficiente.
- [MySQL](https://www.mysql.com/): base de datos relacional.
- [Postman](https://www.postman.com/): herramienta de desarrollo y pruebas de API's.
- [Swagger](https://swagger.io/): es un conjunto de herramientas de código abierto que permite describir, diseñar, crear, documentar y consumir API REST.