from dataclasses import dataclass
from models.financial_entities import FinancialText, FinancialTable
from typing import Optional

@dataclass
class FinancialReportResponse:
    """Represents the response containing financial report data."""

    text: Optional[FinancialText] = None  
    table: Optional[FinancialTable] = None  