from fastapi import APIRouter, Depends
from models.producto_model import Producto
from services.producto_service import agregar_producto, listar_productos
from auth import verificar_token  # importa tu función de validación

router = APIRouter()

@router.post("/productos")
def crear_producto(producto: Producto, usuario: dict = Depends(verificar_token)):
    """
    Crea un nuevo producto en el sistema. Requiere autenticación.

    Args:
        producto (Producto): Datos del producto.
        usuario (dict): Usuario autenticado (extraído del token).

    Returns:
        dict: Mensaje de confirmación.
    """
    agregar_producto(producto)
    return {"mensaje": f"Producto creado exitosamente por {usuario['sub']}"}


@router.get("/productos")
def obtener_productos(usuario: dict = Depends(verificar_token)):
    """
    Lista los productos registrados. Requiere autenticación.

    Args:
        usuario (dict): Usuario autenticado (extraído del token).

    Returns:
        list[dict]: Lista de productos.
    """
    return listar_productos()

