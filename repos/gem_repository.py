from main import engine
from models.gem_models import Gem, GemProperties
from sqlmodel import Session, select, or_


# def select_gems():
#     with Session(engine) as session:
#         statement = select(Gem)
#         # statement = statement.where(Gem.id >1).where(Gem.id <4)
#         # statement = statement.where(or_(Gem.id >2, Gem.price != 1000))
#
#
#         result = session.exec(statement)
#         print(result.all())
#         # result.first()
#
# select_gems()

def select_all_gems():
    with Session(engine) as session:

        statement = select(Gem)
        # statement = select(Gem, GemProperties).where(Gem.gem_properties_id==GemProperties.id)
        result = session.exec(statement)
        return result.all()
