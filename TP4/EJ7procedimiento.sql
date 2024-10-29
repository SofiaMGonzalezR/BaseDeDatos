CREATE PROCEDURE ConsolidarVentas
AS
BEGIN
    DECLARE @ClienteId INT, @ProductoId INT, @Cantidad INT, @PrecioUnitario DECIMAL(10, 2);
    DECLARE @IngresoTotal DECIMAL(15, 2);

    BEGIN TRANSACTION;

    BEGIN TRY
        DECLARE PedidoCursor CURSOR FOR
        SELECT ClienteId, ProductoId, Cantidad, PrecioUnitario
        FROM Pedidos;

        OPEN PedidoCursor;
        FETCH NEXT FROM PedidoCursor INTO @ClienteId, @ProductoId, @Cantidad, @PrecioUnitario;
        WHILE @FETCH_STATUS = 0
        BEGIN
            SET @IngresoTotal = @Cantidad * @PrecioUnitario;
            IF EXISTS (
                SELECT 1 
                FROM ConsolidadoVentas 
                WHERE ClienteId = @ClienteId AND ProductoId = @ProductoId
            )
            BEGIN
                UPDATE ConsolidadoVentas
                SET CantidadTotal = CantidadTotal + @Cantidad,
                    IngresoTotal = IngresoTotal + @IngresoTotal
                WHERE ClienteId = @ClienteId AND ProductoId = @ProductoId;
            END
            ELSE
            BEGIN
                INSERT INTO ConsolidadoVentas (ClienteId, ProductoId, CantidadTotal, IngresoTotal)
                VALUES (@ClienteId, @ProductoId, @Cantidad, @IngresoTotal);
            END
            FETCH NEXT FROM PedidoCursor INTO @ClienteId, @ProductoId, @Cantidad, @PrecioUnitario;
        END
        CLOSE PedidoCursor;
        DEALLOCATE PedidoCursor;
        COMMIT TRANSACTION;
    END TRY
END;
