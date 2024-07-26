from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from backends.settings import settings


Engine = create_engine(settings.DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()
