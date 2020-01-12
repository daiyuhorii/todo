
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import os

class MysqlConfig:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
        **{
            # fix later host to flaskapp_mysql_1
            'user': 'root',
            'password': 'teamnull',
            'host': os.getenv('DB_HOST', 'flaskapp_mysql_1:3306'),
            'database': 'db2019'
        }
    )
    ENGINE = create_engine(SQLALCHEMY_DATABASE_URI, encoding='utf-8', echo=True)
    session = scoped_session(sessionmaker(bind=ENGINE, autocommit=False, autoflush=False))
    Base = declarative_base()
    Base.query = session.query_property()

Config = MysqlConfig
