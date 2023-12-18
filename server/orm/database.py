# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 定义数据库的连接URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./databases/weixin_crawl.db"

# 创建一个数据库引擎
# create_engine负责创建和管理数据库连接，以及执行SQL命令。
# 在此示例中，我们为SQLite数据库提供了特定的连接参数check_same_thread。
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 使用declarative_base创建一个Base类
# declarative_base是一个工厂函数，它为声明式类定义创建一个新的Base类。
# 你的模型类（即数据库表的模型）通常会继承这个Base类。
# 这种方式允许你使用面向对象的方式来定义数据库的表和关系。
Base = declarative_base()
