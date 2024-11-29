---
jupyter:
  colab:
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 5
---

::: {#QuMn1Lbbdz7p .cell .markdown id="QuMn1Lbbdz7p"}
# Código de inicialización

Este código permite inicializar las bibliotecas para usar SQLite en la
máquina virtual de Google Colab. El código además elimina cualquier dato
almacenado anteriormente en el archvio `ejemplos.db`. Es recomendable
volver a correr el código cada vez que se comience con la resolución de
un nuevo ejercicio.
:::

::: {#DRIupxipNuoC .cell .code execution_count="1" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="DRIupxipNuoC" outputId="5b514e5a-9f6a-4b64-e175-1ddc564e8eab"}
``` python
!pip install pymysql
%load_ext sql
!rm -rf ejemplos.db
%sql sqlite:///ejemplos.db
```

::: {.output .stream .stdout}
    Collecting pymysql
      Downloading PyMySQL-1.1.1-py3-none-any.whl.metadata (4.4 kB)
    Downloading PyMySQL-1.1.1-py3-none-any.whl (44 kB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0.0/45.0 kB ? eta -:--:--
    ysql
    Successfully installed pymysql-1.1.1
:::
:::

::: {#cVK-sijYVIH5 .cell .markdown id="cVK-sijYVIH5"}
# EJERCICIOS DE GROUP y HAVING
:::

::: {#NsVx4_K4NiXp .cell .markdown id="NsVx4_K4NiXp"}
## Ejercicio 1: Ventas por Ciudad de distintos insumos informáticos

Tienes dos tablas llamadas `Ventas` y `Productos`:

-   La tabla `Ventas` tiene las siguientes columnas:
    -   `VentaID` (INT)
    -   `ProductoID` (INT, FOREIGN KEY que referencia a
        `Productos(ProductoID)`)
    -   `CantidadVendida` (INT)
    -   `PrecioUnitario` (DECIMAL)
    -   `Ciudad` (VARCHAR)
-   La tabla `Productos` tiene las siguientes columnas:
    -   `ProductoID` (INT, PRIMARY KEY)
    -   `NombreProducto` (VARCHAR)
    -   `Precio` (DECIMAL)

Deseas analizar las ventas por ciudad, combinando la información de
ambas tablas para mostrar el nombre de los productos vendidos y el total
de ingresos generados por cada ciudad.
:::

::: {#k5xOpu04NiXr .cell .code execution_count="4" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="k5xOpu04NiXr" outputId="321fc199-ea95-4e5d-f5e2-fa4a8edade8c"}
``` python
%%sql
-- Escribe aquí el código DDL para crear las tablas Ventas y Productos

CREATE TABLE Productos (
  ProductoID INTEGER PRIMARY KEY,
  NombreProducto VARCHAR(50),
  Precio DECIMAL(10, 2)
);

CREATE TABLE Ventas (
  VentaID INTEGER PRIMARY KEY,
  ProductoID INTEGER,
  CantidadVendida INTEGER,
  PrecioUnitario DECIMAL(10, 2),
  Ciudad VARCHAR(50),
  FOREIGN KEY (ProductoID) REFERENCES Productos(ProductoID)
);
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    (sqlite3.OperationalError) table Productos already exists
    [SQL: -- Escribe aquí el código DDL para crear las tablas Ventas y Productos

    CREATE TABLE Productos (
      ProductoID INTEGER PRIMARY KEY,
      NombreProducto VARCHAR(50),
      Precio DECIMAL(10, 2)
    );]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)
:::
:::

::: {#leRDWrTpQocv .cell .markdown id="leRDWrTpQocv"}
**Codigo DBML de tablas Productos, y Ventas:**
:::

::: {#gLjYEn67Qm_H .cell .code id="gLjYEn67Qm_H"}
``` python
Project Tienda {
  database_type: "SQLite"
}

Table Productos {
  ProductoID int [pk, not null] // Clave primaria
  NombreProducto varchar(50) [not null] // Nombre del producto
  Precio decimal(10, 2) [not null] // Precio del producto

  Note: "Tabla que almacena la información de los productos."
}

Table Ventas {
  VentaID int [pk, not null] // Clave primaria
  ProductoID int [ref: > Productos.ProductoID, not null] // Clave foránea hacia Productos
  CantidadVendida int [not null] // Cantidad vendida
  PrecioUnitario decimal(10, 2) [not null] // Precio unitario del producto
  Ciudad varchar(50) [not null] // Ciudad donde se realizó la venta

  Note: "Tabla que registra las ventas realizadas."
}
```
:::

::: {#tw9GKn4iScVu .cell .markdown id="tw9GKn4iScVu"}
**Codigo DBML de tablas Productos, Ventas:**
:::

::: {#OoSKEHguSguY .cell .markdown id="OoSKEHguSguY"}
:::

::: {#im4yKrVtNiXt .cell .markdown id="im4yKrVtNiXt"}
**Rellenado de la tabla Ventas**
:::

::: {#71b6196d .cell .code execution_count="3" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="71b6196d" outputId="f98eb3e7-2207-4658-98df-dd36ce2296de"}
``` python
# Población de la tabla Ventas
# Insertar datos en la tabla Ventas
%%sql
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (5, 1, 6, 45.00, 'Buenos Aires');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (6, 12, 9, 35.00, 'Córdoba');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (7, 2, 4, 20.00, 'Rosario');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (8, 13, 12, 60.00, 'Mendoza');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (9, 3, 7, 55.00, 'La Plata');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (10, 3, 5, 32.50, 'San Miguel de Tucumán');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (11, 11, 3, 28.00, 'Salta');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (12, 11, 8, 40.00, 'Mar del Plata');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (13, 11, 11, 70.00, 'Santa Fe');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (14, 11, 4, 25.00, 'San Juan');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (15, 11, 9, 35.00, 'Neuquén');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (16, 11, 6, 45.00, 'Posadas');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (17, 13, 10, 50.00, 'Bahía Blanca');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (18, 11, 12, 65.00, 'San Salvador de Jujuy');
INSERT INTO Ventas (VentaID, ProductoID, CantidadVendida, PrecioUnitario, Ciudad) VALUES (19, 15, 3, 22.50, 'Comodoro Rivadavia');

INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (1, 'Teclado Mecánico', 75.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (2, 'Mouse Inalámbrico', 45.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (3, 'Monitor 24 Pulgadas', 150.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (4, 'Disco Duro SSD 1TB', 120.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (5, 'Memoria RAM 16GB', 80.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (6, 'Placa Madre ATX', 200.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (7, 'Tarjeta Gráfica 6GB', 350.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (8, 'Auriculares con Micrófono', 60.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (9, 'Cámara Web HD', 55.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (10, 'Micrófono de Condensador', 90.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (11, 'Router WiFi 6', 130.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (12, 'Impresora Láser', 180.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (13, 'Soporte Monitor Ajustable', 25.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (14, 'Teclado Inalámbrico', 50.00);
INSERT INTO Productos (ProductoID, NombreProducto, Precio) VALUES (15, 'Mouse Gaming', 40.00);

```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
:::

::: {.output .execute_result execution_count="3"}
    []
:::
:::

::: {#622zROEDNiXt .cell .markdown id="622zROEDNiXt"}
**Consignas del ejercicio:**

1.  Encuentre el total de ingresos (`CantidadVendida * PrecioUnitario`)
    por cada ciudad.
:::

::: {#tB0Jv-NuOLyZ .cell .code execution_count="9" id="tB0Jv-NuOLyZ"}
``` python
from prettytable import PrettyTable
from prettytable import TableStyle

# Establecer un estilo de tabla válido
PrettyTable.DEFAULT = TableStyle
```
:::

::: {#zuIw9B9UNiXu .cell .code execution_count="11" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":389}" id="zuIw9B9UNiXu" outputId="8714b4e3-e64f-44fa-93b1-368c835d41d1"}
``` python
%%sql
SELECT
    Ciudad,
    SUM(CantidadVendida * PrecioUnitario) AS TotalIngresos
FROM
    Ventas
GROUP BY
    Ciudad;
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="11"}
```{=html}
<table>
    <thead>
        <tr>
            <th>Ciudad</th>
            <th>TotalIngresos</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Bahía Blanca</td>
            <td>500</td>
        </tr>
        <tr>
            <td>Buenos Aires</td>
            <td>270</td>
        </tr>
        <tr>
            <td>Comodoro Rivadavia</td>
            <td>67.5</td>
        </tr>
        <tr>
            <td>Córdoba</td>
            <td>315</td>
        </tr>
        <tr>
            <td>La Plata</td>
            <td>385</td>
        </tr>
        <tr>
            <td>Mar del Plata</td>
            <td>320</td>
        </tr>
        <tr>
            <td>Mendoza</td>
            <td>720</td>
        </tr>
        <tr>
            <td>Neuquén</td>
            <td>315</td>
        </tr>
        <tr>
            <td>Posadas</td>
            <td>270</td>
        </tr>
        <tr>
            <td>Rosario</td>
            <td>80</td>
        </tr>
        <tr>
            <td>Salta</td>
            <td>84</td>
        </tr>
        <tr>
            <td>San Juan</td>
            <td>100</td>
        </tr>
        <tr>
            <td>San Miguel de Tucumán</td>
            <td>162.5</td>
        </tr>
        <tr>
            <td>San Salvador de Jujuy</td>
            <td>780</td>
        </tr>
        <tr>
            <td>Santa Fe</td>
            <td>770</td>
        </tr>
    </tbody>
</table>
```
:::
:::

::: {#b96bb132 .cell .markdown id="b96bb132"}
1.  Escriba el código SQL para listar las Ciudades cuyo total de
    ingresos supera los \$500.
:::

::: {#ACqNMaDGNiXu .cell .code execution_count="12" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":137}" id="ACqNMaDGNiXu" outputId="11520f0d-c37c-4293-b976-efb4018bacbd"}
``` python
%%sql
SELECT
    Ciudad,
    SUM(CantidadVendida * PrecioUnitario) AS TotalIngresos
FROM
    Ventas
GROUP BY
    Ciudad
HAVING
    SUM(CantidadVendida * PrecioUnitario) > 500;
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="12"}
```{=html}
<table>
    <thead>
        <tr>
            <th>Ciudad</th>
            <th>TotalIngresos</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Mendoza</td>
            <td>720</td>
        </tr>
        <tr>
            <td>San Salvador de Jujuy</td>
            <td>780</td>
        </tr>
        <tr>
            <td>Santa Fe</td>
            <td>770</td>
        </tr>
    </tbody>
</table>
```
:::
:::

::: {#7a6a43fe .cell .markdown id="7a6a43fe"}
*3*. Modifique la consulta del inciso 2 para ordenar las Ciudades de
mayor a menor ingreso total.
:::

::: {#kzhBe0qENiXv .cell .code execution_count="13" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":137}" id="kzhBe0qENiXv" outputId="136572ed-8415-40f4-8dfc-2e8ca23f986e"}
``` python
%%sql
SELECT
    Ciudad,
    SUM(CantidadVendida * PrecioUnitario) AS TotalIngresos
FROM
    Ventas
GROUP BY
    Ciudad
HAVING
    SUM(CantidadVendida * PrecioUnitario) > 500
ORDER BY
    TotalIngresos DESC;
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="13"}
```{=html}
<table>
    <thead>
        <tr>
            <th>Ciudad</th>
            <th>TotalIngresos</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>San Salvador de Jujuy</td>
            <td>780</td>
        </tr>
        <tr>
            <td>Santa Fe</td>
            <td>770</td>
        </tr>
        <tr>
            <td>Mendoza</td>
            <td>720</td>
        </tr>
    </tbody>
</table>
```
:::
:::

::: {#fRufPLTENiXv .cell .markdown id="fRufPLTENiXv"}
## Ejercicio 2: Promedio de Calificaciones por Curso

Considera las siguientes tres tablas:

-   La tabla **Estudiantes** contiene información sobre los estudiantes
    inscritos:
    -   `EstudianteID` (INT, PRIMARY KEY)
    -   `Nombre` (VARCHAR)
-   La tabla **Cursos** contiene información sobre los cursos
    disponibles:
    -   `CursoID` (INT, PRIMARY KEY)
    -   `NombreCurso` (VARCHAR)
-   La tabla **Calificaciones** registra las notas de los estudiantes en
    los cursos:
    -   `CalificacionID` (INT, PRIMARY KEY)
    -   `EstudianteID` (INT, FOREIGN KEY que referencia a
        `Estudiantes(EstudianteID)`)
    -   `CursoID` (INT, FOREIGN KEY que referencia a `Cursos(CursoID)`)
    -   `Nota` (DECIMAL)

En este ejercicio, debes analizar el rendimiento de los estudiantes en
cada curso, combinando la información de las tres tablas.
:::

::: {#xd4jJS-oNiXv .cell .code execution_count="14" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="xd4jJS-oNiXv" outputId="37b2f76c-2570-4e7d-b657-754cf2a2c7a3"}
``` python
%%sql
-- Crear tabla Estudiantes
CREATE TABLE Estudiantes (
    EstudianteID INTEGER PRIMARY KEY,
    Nombre VARCHAR(50)
);

-- Crear tabla Cursos
CREATE TABLE Cursos (
    CursoID INTEGER PRIMARY KEY,
    NombreCurso VARCHAR(50)
);

-- Crear tabla Calificaciones
CREATE TABLE Calificaciones (
    CalificacionID INTEGER PRIMARY KEY,
    EstudianteID INTEGER,
    CursoID INTEGER,
    Nota DECIMAL(5, 2),
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(EstudianteID),
    FOREIGN KEY (CursoID) REFERENCES Cursos(CursoID)
);
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
    Done.
    Done.
:::

::: {.output .execute_result execution_count="14"}
    []
:::
:::

::: {#rkGPLYCkRLHr .cell .markdown id="rkGPLYCkRLHr"}
**Codigo DBML de tablas SistemaEducativo, Estudiante, Calificaciones:**
:::

::: {#n4jNBvKZRICM .cell .code id="n4jNBvKZRICM"}
``` python
Project SistemaEducativo {
  database_type: "SQLite"
}

Table Estudiantes {
  EstudianteID int [pk, not null] // Clave primaria
  Nombre varchar(50) [not null] // Nombre del estudiante

  Note: "Tabla que almacena información de los estudiantes."
}

Table Cursos {
  CursoID int [pk, not null] // Clave primaria
  NombreCurso varchar(50) [not null] // Nombre del curso

  Note: "Tabla que almacena información de los cursos."
}

Table Calificaciones {
  CalificacionID int [pk, not null] // Clave primaria
  EstudianteID int [ref: > Estudiantes.EstudianteID, not null] // Clave foránea hacia Estudiantes
  CursoID int [ref: > Cursos.CursoID, not null] // Clave foránea hacia Cursos
  Nota decimal(5, 2) [not null] // Nota del estudiante en el curso

  Note: "Tabla que almacena las calificaciones de los estudiantes en los cursos."
}
```
:::

::: {#PetPTF2_R-A5 .cell .markdown id="PetPTF2_R-A5"}
**Diagrama generado:**
:::

::: {#aamKx607SDrr .cell .markdown id="aamKx607SDrr"}
:::

::: {#urovVyAXNiXw .cell .markdown id="urovVyAXNiXw"}
**Población de la tabla Calificaciones**
:::

::: {#fqMJXxAUNiXw .cell .code execution_count="15" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="fqMJXxAUNiXw" outputId="5620afdc-d7d1-46e3-eafd-62994634a64a"}
``` python
# Insertar datos en la tabla Calificaciones
%%sql

INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1001, 'Carlos');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1002, 'Maria');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1003, 'Juan');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1004, 'Ana');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1005, 'Luis');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1006, 'Sofia');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1007, 'Diego');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1008, 'Laura');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1009, 'Javier');
INSERT INTO Estudiantes (EstudianteID, Nombre) VALUES (1010, 'Fernanda');

INSERT INTO Cursos (CursoID, NombreCurso) VALUES (201, 'Matemáticas');
INSERT INTO Cursos (CursoID, NombreCurso) VALUES (202, 'Historia');
INSERT INTO Cursos (CursoID, NombreCurso) VALUES (203, 'Ciencias');
INSERT INTO Cursos (CursoID, NombreCurso) VALUES (204, 'Literatura');
INSERT INTO Cursos (CursoID, NombreCurso) VALUES (205, 'Geografía');

INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (1, 1001, 201, 88.5);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (2, 1002, 202, 92.0);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (3, 1003, 201, 81.0);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (4, 1004, 203, 79.5);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (5, 1005, 202, 84.0);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (6, 1006, 204, 91.5);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (7, 1007, 205, 75.5);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (8, 1008, 204, 87.0);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (9, 1009, 203, 82.5);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (10, 1010, 205, 78.0);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (11, 1002, 201, 90.0);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (12, 1006, 202, 88.0);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (13, 1003, 203, 85.0);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (14, 1007, 201, 80.5);
INSERT INTO Calificaciones (CalificacionID, EstudianteID, CursoID, Nota) VALUES (15, 1005, 204, 89.5);
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
:::

::: {.output .execute_result execution_count="15"}
    []
:::
:::

::: {#fxLxg4M1NiXw .cell .markdown id="fxLxg4M1NiXw"}
**Consignas del ejercicio:**

1.  Encuentre el promedio de `Nota` para cada `Curso`.
:::

::: {#zMGp3kBgNiXw .cell .code execution_count="16" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":179}" id="zMGp3kBgNiXw" outputId="4a775340-be35-46f1-818a-f8cbd7a511bf"}
``` python
%%sql
SELECT
    c.NombreCurso,
    AVG(cal.Nota) AS PromedioNota
FROM
    Calificaciones cal
JOIN
    Cursos c ON cal.CursoID = c.CursoID
GROUP BY
    c.NombreCurso;
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="16"}
```{=html}
<table>
    <thead>
        <tr>
            <th>NombreCurso</th>
            <th>PromedioNota</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ciencias</td>
            <td>82.33333333333333</td>
        </tr>
        <tr>
            <td>Geografía</td>
            <td>76.75</td>
        </tr>
        <tr>
            <td>Historia</td>
            <td>88.0</td>
        </tr>
        <tr>
            <td>Literatura</td>
            <td>89.33333333333333</td>
        </tr>
        <tr>
            <td>Matemáticas</td>
            <td>85.0</td>
        </tr>
    </tbody>
</table>
```
:::
:::

::: {#722c022c .cell .markdown id="722c022c"}
1.  Escriba el código SQL para listar los cursos con un promedio mayor a
    85.
:::

::: {#w_YVVudPNiXx .cell .code execution_count="17" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":116}" id="w_YVVudPNiXx" outputId="602144b3-68b4-4a1f-ace2-f581b918df4b"}
``` python
%%sql
SELECT
    c.NombreCurso,
    AVG(cal.Nota) AS PromedioNota
FROM
    Calificaciones cal
JOIN
    Cursos c ON cal.CursoID = c.CursoID
GROUP BY
    c.NombreCurso
HAVING
    AVG(cal.Nota) > 85;
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="17"}
```{=html}
<table>
    <thead>
        <tr>
            <th>NombreCurso</th>
            <th>PromedioNota</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Historia</td>
            <td>88.0</td>
        </tr>
        <tr>
            <td>Literatura</td>
            <td>89.33333333333333</td>
        </tr>
    </tbody>
</table>
```
:::
:::

::: {#04841eea .cell .markdown id="04841eea"}
1.  Agregue una columna que muestre el número de estudiantes que han
    tomado cada curso cuyo promedio supera 85, ordenados en forma
    descendente por promedio.
:::

::: {#TBh31bsgNiXx .cell .code execution_count="18" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":116}" id="TBh31bsgNiXx" outputId="987b7d07-22e7-4cfc-bac3-99925c021f68"}
``` python
%%sql
SELECT
    c.NombreCurso,
    AVG(cal.Nota) AS PromedioNota,
    COUNT(cal.EstudianteID) AS NumeroEstudiantes
FROM
    Calificaciones cal
JOIN
    Cursos c ON cal.CursoID = c.CursoID
GROUP BY
    c.NombreCurso
HAVING
    AVG(cal.Nota) > 85
ORDER BY
    PromedioNota DESC;
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="18"}
```{=html}
<table>
    <thead>
        <tr>
            <th>NombreCurso</th>
            <th>PromedioNota</th>
            <th>NumeroEstudiantes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Literatura</td>
            <td>89.33333333333333</td>
            <td>3</td>
        </tr>
        <tr>
            <td>Historia</td>
            <td>88.0</td>
            <td>3</td>
        </tr>
    </tbody>
</table>
```
:::
:::

::: {#ReFeNTPaNiXx .cell .markdown id="ReFeNTPaNiXx"}
## Ejercicio 3: Conteo de Empleados por Departamento

Tienes dos tablas llamadas `Empleados` y `Departamentos`:

-   La tabla `Empleados` tiene las siguientes columnas:
    -   `EmpleadoID` (INT)
    -   `Nombre` (VARCHAR)
    -   `DepartamentoID` (INT, FOREIGN KEY que referencia a
        `Departamentos(DepartamentoID)`)
    -   `Salario` (DECIMAL)
-   La tabla `Departamentos` tiene las siguientes columnas:
    -   `DepartamentoID` (INT, PRIMARY KEY)
    -   `NombreDepartamento` (VARCHAR)

Deseas analizar la distribución de empleados en cada departamento,
combinando la información de ambas tablas para mostrar el nombre del
departamento y el número de empleados por cada uno.

**Consignas a responder:**
:::

::: {#TM-JwO9TNiXy .cell .code execution_count="21" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="TM-JwO9TNiXy" outputId="08cdd453-f95f-49b4-9959-749612988c99"}
``` python
%%sql
-- Crear la tabla Departamentos
CREATE TABLE Departamentos (
    DepartamentoID INT PRIMARY KEY,
    NombreDepartamento VARCHAR(255) NOT NULL
);

-- Crear la tabla Empleados
CREATE TABLE Empleados (
    EmpleadoID INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    DepartamentoID INT,
    Salario DECIMAL(10, 2),
    FOREIGN KEY (DepartamentoID) REFERENCES Departamentos(DepartamentoID)
);
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="21"}
    []
:::
:::

::: {#pcBLQS94Rn6- .cell .markdown id="pcBLQS94Rn6-"}
Codigo DMBL de tablas Departamentos, Empleados:
:::

::: {#zL1ZsSmpRnpX .cell .code id="zL1ZsSmpRnpX"}
``` python
Project Empresa {
  database_type: "SQLite"
}

Table Departamentos {
  DepartamentoID int [pk, not null] // Clave primaria
  NombreDepartamento varchar(255) [not null] // Nombre del departamento

  Note: "Tabla que almacena información sobre los departamentos."
}

Table Empleados {
  EmpleadoID int [pk, not null] // Clave primaria
  Nombre varchar(255) [not null] // Nombre del empleado
  DepartamentoID int [ref: > Departamentos.DepartamentoID, not null] // Clave foránea hacia Departamentos
  Salario decimal(10, 2) [not null] // Salario del empleado

  Note: "Tabla que almacena información sobre los empleados, incluyendo su salario y departamento."
}
```
:::

::: {#tMLUf24nSqQX .cell .markdown id="tMLUf24nSqQX"}
**Codigo DBML de tablas Departamentos, Empleados:**
:::

::: {#OyWxJRZtSukw .cell .markdown id="OyWxJRZtSukw"}
:::

::: {#50OKu9KYNiXy .cell .markdown id="50OKu9KYNiXy"}
**Relleno de las tablas `Empleados` y `Departamentos`**
:::

::: {#6GvQ-IV1NiXy .cell .code execution_count="22" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="6GvQ-IV1NiXy" outputId="a9c223b0-ba0a-4ef5-85d7-a374bb54328e"}
``` python
%%sql
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (5, 'Laura', 101, 3100);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (6, 'Javier', 104, 3300);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (7, 'Sofia', 105, 2900);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (8, 'Lucas', 105, 3700);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (9, 'Fernanda', 101, 3200);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (10, 'Diego', 104, 3400);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (11, 'Martina', 103, 4000);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (12, 'Gustavo', 105, 2950);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (13, 'Liliana', 106, 3800);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (14, 'Gabriel', 106, 4100);
INSERT INTO Empleados (EmpleadoID, Nombre, DepartamentoID, Salario) VALUES (15, 'Natalia', 102, 3600);

INSERT INTO Departamentos (DepartamentoID, NombreDepartamento) VALUES (101, 'Marketing');
INSERT INTO Departamentos (DepartamentoID, NombreDepartamento) VALUES (102, 'Ventas');
INSERT INTO Departamentos (DepartamentoID, NombreDepartamento) VALUES (103, 'Recursos Humanos');
INSERT INTO Departamentos (DepartamentoID, NombreDepartamento) VALUES (104, 'Desarrollo de Producto');
INSERT INTO Departamentos (DepartamentoID, NombreDepartamento) VALUES (105, 'Investigación de Mercado');
INSERT INTO Departamentos (DepartamentoID, NombreDepartamento) VALUES (106, 'Atención al Cliente');
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
:::

::: {.output .execute_result execution_count="22"}
    []
:::
:::

::: {#Oy_3JkD3NiXy .cell .markdown id="Oy_3JkD3NiXy"}
**Consignas del ejercicio:**

1.  Encuentre el número total de empleados en cada departamento.
:::

::: {#Z9-3BGMFNiXy .cell .code execution_count="23" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":200}" id="Z9-3BGMFNiXy" outputId="68bf5db3-6279-41d3-a711-507411f9ab86"}
``` python
%%sql
SELECT d.NombreDepartamento, COUNT(e.EmpleadoID) AS TotalEmpleados
FROM Departamentos d
LEFT JOIN Empleados e ON d.DepartamentoID = e.DepartamentoID
GROUP BY d.DepartamentoID;
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="23"}
```{=html}
<table>
    <thead>
        <tr>
            <th>NombreDepartamento</th>
            <th>TotalEmpleados</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Marketing</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Ventas</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Recursos Humanos</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Desarrollo de Producto</td>
            <td>2</td>
        </tr>
        <tr>
            <td>Investigación de Mercado</td>
            <td>3</td>
        </tr>
        <tr>
            <td>Atención al Cliente</td>
            <td>2</td>
        </tr>
    </tbody>
</table>
```
:::
:::

::: {#dd365a64 .cell .markdown id="dd365a64"}
**2**. Escriba el código SQL para listar los departamentos que tienen
más de 2 empleados.
:::

::: {#UYodiO03NiXy .cell .code execution_count="24" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":95}" id="UYodiO03NiXy" outputId="1f4931a2-5426-4b78-816f-2cfb390aa7fc"}
``` python
%%sql
SELECT d.NombreDepartamento, COUNT(e.EmpleadoID) AS TotalEmpleados
FROM Departamentos d
JOIN Empleados e ON d.DepartamentoID = e.DepartamentoID
GROUP BY d.DepartamentoID
HAVING COUNT(e.EmpleadoID) > 2;

```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="24"}
```{=html}
<table>
    <thead>
        <tr>
            <th>NombreDepartamento</th>
            <th>TotalEmpleados</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Investigación de Mercado</td>
            <td>3</td>
        </tr>
    </tbody>
</table>
```
:::
:::

::: {#67a157bb .cell .markdown id="67a157bb"}
1.  Muestre el salario promedio de los empleados por cada departamento
    ordenados promedio en forma descendente.
:::

::: {#xfVqujA5NiXy .cell .code execution_count="25" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":200}" id="xfVqujA5NiXy" outputId="b5474881-bfe0-47d7-b69b-aad7c7fbc300"}
``` python
%%sql
SELECT d.NombreDepartamento, AVG(e.Salario) AS PromedioSalario
FROM Departamentos d
JOIN Empleados e ON d.DepartamentoID = e.DepartamentoID
GROUP BY d.DepartamentoID
ORDER BY PromedioSalario DESC;
```

::: {.output .stream .stdout}
     * sqlite:///ejemplos.db
    Done.
:::

::: {.output .execute_result execution_count="25"}
```{=html}
<table>
    <thead>
        <tr>
            <th>NombreDepartamento</th>
            <th>PromedioSalario</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Recursos Humanos</td>
            <td>4000.0</td>
        </tr>
        <tr>
            <td>Atención al Cliente</td>
            <td>3950.0</td>
        </tr>
        <tr>
            <td>Ventas</td>
            <td>3600.0</td>
        </tr>
        <tr>
            <td>Desarrollo de Producto</td>
            <td>3350.0</td>
        </tr>
        <tr>
            <td>Investigación de Mercado</td>
            <td>3183.3333333333335</td>
        </tr>
        <tr>
            <td>Marketing</td>
            <td>3150.0</td>
        </tr>
    </tbody>
</table>
```
:::
:::