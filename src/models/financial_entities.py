from dataclasses import dataclass
from typing import List

@dataclass
class FinancialEntity:
    """Base class for financial entities."""
    pass

@dataclass
class FinancialText(FinancialEntity):
    """Represents text content in a financial report."""
    content: str

@dataclass
class FinancialTable(FinancialEntity):
    """Represents table data in a financial report."""
    data: List[list]