from typing import Optional

from sqlmodel import SQLModel, Field
from enum import Enum, IntEnum


class GemClarity(IntEnum):
    SI = 1
    VS = 2
    vvs = 3
    FL = 4


class GemTypes(str, Enum):
    DIAMOND = 'DIAMOND'
    RUBY = 'RUBY'
    EMERALD = 'EMERALD'


class GemColor(str, Enum):
    D = 'D'
    E = 'E'
    G = 'G'
    F = 'F'
    H = 'H'
    I = 'I'


class GemProperties(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    size: float = 1
    clarity: Optional[GemClarity] = None
    color: Optional[GemColor] = None


class Gem(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    price: float
    available: bool = True
    gem_type : GemTypes = GemTypes.DIAMOND

    gem_properties_id: Optional[int] = Field(default=None, foreign_key='gemproperties.id')
