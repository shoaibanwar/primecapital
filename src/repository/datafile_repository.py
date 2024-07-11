#Financial DataMapper for Datafile
from .repository_interface import FinancialRepositoryInterface
from models.financial_entities import FinancialText


class FinancialDataFileRepository(FinancialRepositoryInterface):
    """Repository for fetching financial data from a file."""

    def __init__(self, source_path: str) -> None:
        self.source: str = source_path

    def get_all_data(self) -> FinancialText:
        """Fetches all financial data from the file."""
        try:
            with open(self.source, 'r') as file:
                data = file.readlines()
                file_data = [line.strip() for line in data]
                return FinancialText(content=file_data[0])
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            raise e