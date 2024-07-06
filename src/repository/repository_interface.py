#FinancialDataMapper Interface
from abc import ABC, abstractmethod
from models.financial_entities import FinancialEntity

class FinancialRepositoryInterface(ABC):
    """Interface for financial data repositories."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all_data(self) -> FinancialEntity:
       """Fetches all financial data from the repository."""
       pass