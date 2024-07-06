#Financial DataMapper for Database

from repository.repository_interface import FinancialRepositoryInterface
from models.financial_database import FinancialDatabase
from models.financial_entities import FinancialTable


class FinancialDataBaseRepository(FinancialRepositoryInterface):
    """Repository for fetching financial data from a database."""

    def __init__(self, source_path: str) -> None:
        self.source: FinancialDatabase = FinancialDatabase(source_path)

    def get_all_data(self) -> FinancialTable:
        """Fetches all financial data from the database."""
        return self.source.get_all_data()