from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    total_balance = Column(Float, default=0.0)
    transactions = relationship("Transaction", back_populates="user")

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String(20), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
    user = relationship("User", back_populates="transactions")

# Create database and tables
engine = create_engine('sqlite:///banking.db')
Base.metadata.create_all(engine)

# Create session factory
Session = sessionmaker(bind=engine)
