-- Creación de Base de Datos
CREATE DATABASE IF NOT EXISTS Biblioteca;
USE Biblioteca;

-- Tabla Usuarios
CREATE TABLE Usuarios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Direccion VARCHAR(255),
    FechaRegistro DATE NOT NULL,
    UNIQUE (Nombre)
);

-- Tabla Libros
CREATE TABLE Libros (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Titulo VARCHAR(255) NOT NULL,
    Autor VARCHAR(100) NOT NULL,
    Genero VARCHAR(50),
    AnioPublicacion YEAR NOT NULL,
    UNIQUE (Titulo, Autor)
);

-- Tabla Prestamos
CREATE TABLE Prestamos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    UsuarioID INT NOT NULL,
    LibroID INT NOT NULL,
    FechaPrestamo DATE NOT NULL,
    FechaDevolucion DATE,
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (LibroID) REFERENCES Libros(ID) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Tabla Pagos
CREATE TABLE Pagos (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    UsuarioID INT NOT NULL,
    FechaPago DATE NOT NULL,
    Monto DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Índices
CREATE INDEX idx_nombre_usuarios ON Usuarios (Nombre);
CREATE INDEX idx_prestamos_usuario_fecha ON Prestamos (UsuarioID, FechaPrestamo);

-- Datos Iniciales - Usuarios
INSERT INTO Usuarios (Nombre, Direccion, FechaRegistro)
VALUES
('Juan Pérez', 'Calle Falsa 123', '2023-01-15'),
('María López', 'Av. Siempre Viva 742', '2022-02-10'),
('Carlos Gómez', 'Pasaje Azul 45', '2022-03-20'),
('Ana Martínez', 'Calle Roja 78', '2023-04-01'),
('Luis Torres', 'Av. Verde 90', '2022-05-18'),
('Sofía Herrera', 'Calle Amarilla 65', '2022-06-10'),
('Pedro Domínguez', 'Plaza Central 12', '2023-07-30'),
('Laura Morales', 'Av. Libertad 345', '2023-08-05'),
('Jorge Ramírez', 'Calle Negra 87', '2022-09-14'),
('Paula Fernández', 'Av. Sol 111', '2023-10-22');

-- Datos Iniciales - Libros (modificando AnioPublicacion fuera del rango)
INSERT INTO Libros (Titulo, Autor, Genero, AnioPublicacion)
VALUES
('Cien años de soledad', 'Gabriel García Márquez', 'Novela', 1967),
('1984', 'George Orwell', 'Distopía', 1949),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Clásico', 1605),
('El Principito', 'Antoine de Saint-Exupéry', 'Fábula', 1943),
('Orgullo y Prejuicio', 'Jane Austen', 'Romance', 1813),
('Crimen y Castigo', 'Fiódor Dostoyevski', 'Novela', 1866),
('El Aleph', 'Jorge Luis Borges', 'Cuento', 1949),
('Rayuela', 'Julio Cortázar', 'Novela', 1963),
('La Odisea', 'Homero', 'Épico', 800),  -- Año corregido
('Fausto', 'Johann Wolfgang von Goethe', 'Drama', 1808);

-- Datos Iniciales - Préstamos (asegurando que los LibroID existan en la tabla Libros)
INSERT INTO Prestamos (UsuarioID, LibroID, FechaPrestamo, FechaDevolucion)
VALUES
(1, 1, '2023-01-16', '2023-02-16'),
(2, 2, '2023-03-01', NULL),
(3, 3, '2023-04-10', '2023-05-10'),
(4, 4, '2023-06-15', NULL);  -- LibroID 4 (El Principito) debe existir

-- Datos Iniciales - Pagos
INSERT INTO Pagos (UsuarioID, FechaPago, Monto)
VALUES
(1, '2023-01-10', 100.00),
(2, '2023-02-10', 120.00),
(3, '2023-03-10', 90.00),
(4, '2023-04-10', 110.00),
(5, '2023-05-10', 130.00);
