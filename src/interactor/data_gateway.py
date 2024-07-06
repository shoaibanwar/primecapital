from abc import ABC, abstractmethod
from repository.datafile_repository import FinancialRepositoryInterface
from models.financial_entities import FinancialEntity

class FinancialDataGatewatInterface(ABC):
    """Interface for fetching financial data."""

    def __init__(self, financial_repository: FinancialRepositoryInterface) -> None:
        self.financial_repository: FinancialRepositoryInterface = financial_repository

    @abstractmethod
    def fetch_data(self) -> FinancialEntity:
        """Fetches financial data from the repository."""
        pass


class FinancialDataGateway(FinancialDataGatewatInterface):
    """Fetches financial data from the repository."""

    def __init__(self, financial_repository: FinancialRepositoryInterface) -> None:
        self.financial_repository: FinancialRepositoryInterface = financial_repository

    def fetch_data(self) -> FinancialEntity:
        """Fetches financial data from the repository."""
        data: FinancialEntity = self.financial_repository.get_all_data()
        return data