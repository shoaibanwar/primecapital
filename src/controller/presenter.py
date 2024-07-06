from abc import ABC, abstractmethod
from models.report_request import FinancialReportRequest
from models.report_response import FinancialReportResponse
from interactor.report_generator import FinancialReportGenerator
import config

class FinancialReportPresenter(ABC):
    @abstractmethod
    def handle_request(self):
        pass


class Presenter(FinancialReportPresenter):
    def handle_request(self):
        """Handles the request for financial report generation and returns the response data."""
        report_request = FinancialReportRequest(("TABLE", "TEXT"))
        data: FinancialReportResponse = report_request.manage()
        report_generator:FinancialReportGenerator = FinancialReportGenerator(data, config.OUTPUT_PDF_PATH)
        report_generator.generate_report()
        return data