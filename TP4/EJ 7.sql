CREATE TABLE Pedidos (
    PedidoId INT PRIMARY KEY IDENTITY(1,1),
    ClienteId INT NOT NULL,
    ProductoId INT NOT NULL,
    Cantidad INT NOT NULL,
    PrecioUnitario DECIMAL(10,2) NOT NULL,
    FechaPedido DATE NOT NULL
);

CREATE TABLE ConsolidadoVentas (
    ConsolidadoId INT PRIMARY KEY IDENTITY(1,1),
    ClienteId INT NOT NULL,
    ProductoId INT NOT NULL,
    CantidadTotal INT NOT NULL,
    IngresoTotal DECIMAL(15,2) NOT NULL
);