from tienda_electronicos.tienda import TiendaGestionProductos, TiendaGestionReporteYAnalisis, TiendaGestorDatabase, ElectronicosGestion
from tienda_electronicos.dependencies.container import database, productos_repo, clientes_repo, ventas_repo, detalle_ventas_repo

# productos_repository=productos_repo,
#     clientes_repository=clientes_repo,
#     ventas_repository=ventas_repo,
#     detalle_ventas_repository=detalle_ventas_repo,
# tienda_gestion_compras = TiendaGestionCompras()


tienda_gestion_productos = TiendaGestionProductos(
    productos_repo=productos_repo,
    clientes_repo=clientes_repo
)



# tienda_gestion_graficos_reportes = TiendaGestionGraficosYReportes()


tienda_gestion_reportes_analisis = TiendaGestionReporteYAnalisis(
    detalle_ventas_repository=detalle_ventas_repo,
    clientes_repository=clientes_repo,
    productos_repository=productos_repo,
    db=database
)
