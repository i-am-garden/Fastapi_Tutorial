from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL 데이터베이스에 연결하기 위한 URL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://gardenko:gardenkio@127.0.0.1:8002/testdb"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@hostname:port/database_name"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


