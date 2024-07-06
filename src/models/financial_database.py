import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.session import Session
from models.financial_entities import FinancialTable

Base = declarative_base()

class FinancialReport(Base):
    __tablename__ = 'financial_report'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)

class FinancialDatabase:
    """Handles database operations for financial reports."""
    def __init__(self, db_path: str) -> None:
        self.engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)


    def get_all_data(self) -> FinancialTable:
        """Fetches all financial report data from the database."""
        session: Session = self.Session()
        reports = session.query(FinancialReport).all()
        report_data = [[report.id, report.name, report.amount] for report in reports]
        return FinancialTable(data=report_data)
    

    def close(self) -> None:
        """Closes the database connection."""
        self.engine.dispose()