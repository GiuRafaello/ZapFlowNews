from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):

    produto1 = "Destino Complexo"
    produto2 = "Travesso Destino"
    produto3 = "Destino de amar"

class Vendas(BaseModel):

    """
    Modelo de dados para as vendas.

    Args:

    email ( EmailStr): email do comprador
    data (datetime): data da compra
    valor ( PositiveFloat): valor da compra
    produto ( PositiveInt): nomde do produto
    quantidade(PositiveInt): quantidade do produto
    produto(ProdutoEnum): categoria do produto


    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    produto : ProdutoEnum
    quantidade: PositiveInt 

