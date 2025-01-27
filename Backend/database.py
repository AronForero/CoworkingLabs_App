import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

username = os.environ["DB_USERNAME"]
password = os.environ["DB_PASSWORD"]
# Connection string de PostgreSQL
DATABASE_URL = f"postgresql://{username}:{password}@localhost:5432/coworkinglabs"

# Configuración del engine
engine = create_engine(DATABASE_URL)

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()
