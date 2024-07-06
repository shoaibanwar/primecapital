from abc import ABC, abstractmethod
from models.report_response import FinancialReportResponse
from models.financial_entities import FinancialTable, FinancialText

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table as RLTable, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

class FinancialReportRequestor(ABC):
    """Abstract base class for generating financial reports."""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def generate_report(self) -> None:
        pass

class FinancialReportGenerator(FinancialReportRequestor):
    """Generates a financial report in PDF format."""

    def __init__(self, data: FinancialReportResponse, filename: str) -> None:
        self.text: FinancialText = data.text
        self.table: FinancialTable = data.table
        self.filename: str = filename

    def generate_report(self) -> None:
        """Generates the financial report PDF."""
        doc = SimpleDocTemplate(self.filename, pagesize=letter)
        styles = getSampleStyleSheet()
        flowables = []

        # Add paragraph
        flowables.append(Paragraph(self.text.content, styles['Normal']))

        # Add table
        data = [["ID", "Name", "Amount"]] + self.table.data
        table = RLTable(data)
        flowables.append(table)

        doc.build(flowables)