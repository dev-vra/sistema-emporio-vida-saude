
from sqlalchemy import Column, Integer, String, Float
from database import Base
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String, nullable=True)
    preco_venda = Column(Float, nullable=False)
    preco_custo = Column(Float, nullable=True)
    estoque_atual = Column(Integer, default=0)