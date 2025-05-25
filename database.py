# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "postgresql://envirosensedb_user:rkNngiLgzhr6AQlLiywstBPl4gARlKZ5@dpg-d0kapsjuibrs739chbvg-a.singapore-postgres.render.com/envirosensedb"

engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
