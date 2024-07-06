from enum import Enum
from typing import Tuple
from repository.datafile_repository import FinancialDataFileRepository
from repository.database_repository import  FinancialDataBaseRepository
from repository.repository_interface import FinancialRepositoryInterface
from interactor.data_gateway import FinancialDataGateway
from models.report_response import FinancialReportResponse
from models.financial_entities import FinancialEntity
import config

class RepositoryEnum(Enum):
    """Enum representing the repository types and their parameters."""
    TABLE = [FinancialDataBaseRepository, config.DATABASE_PATH]
    TEXT = [FinancialDataFileRepository , config.DATAFILE_PATH]

    @property
    def get_class(self) -> FinancialRepositoryInterface:
        """Returns the repository class."""
        cls, param = self.value
        return cls

    @property
    def get_params(self) -> str:
        """Returns the repository parameter (path)."""
        cls, param = self.value
        return param
    

class FinancialReportRequest:
    """Handles the request for generating a financial report."""

    def __init__(self, request: Tuple[RepositoryEnum, ...]) -> None:
        self.request = request

    def manage(self) -> FinancialReportResponse:
        """Manages the financial report generation process."""
        response = FinancialReportResponse()
        for key in self.request:
            try:
                # From the enum class, access the object member dynamically using the key
                repo_instance: FinancialRepositoryInterface = RepositoryEnum[key].get_class(RepositoryEnum[key].get_params)
                gateway: FinancialDataGateway = FinancialDataGateway(repo_instance)
                result: FinancialEntity = gateway.fetch_data()
                setattr(response, key.lower(), result)
            except KeyError as ke:
                print(f"Invalid repository key: {key}")
                raise ke
            except Exception as e:
                print(f"Error processing {key}: {str(e)}")
                raise e

        return response