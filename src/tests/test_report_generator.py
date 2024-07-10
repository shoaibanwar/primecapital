import unittest
from unittest.mock import patch
from models.report_response import FinancialReportResponse, FinancialText, FinancialTable
from interactor.report_generator import FinancialReportGenerator

class FinancialReportGeneratorTestCase(unittest.TestCase):
    mock_table_data = [[1, 'Test Report', 100.0]]
    mock_text_data = 'Sample Text'
    mock_file = 'test.pdf'

    @staticmethod
    def get_mock_financial_report_response():
        return FinancialReportResponse(
            text=FinancialText(content=FinancialReportGeneratorTestCase.mock_text_data),
            table=FinancialTable(data=FinancialReportGeneratorTestCase.mock_table_data)
        )

    @patch('interactor.report_generator.SimpleDocTemplate')
    def test_generate_report(self, MockDocTemplate):
        mock_doc_instance = MockDocTemplate.return_value

        data = self.get_mock_financial_report_response()

        generator = FinancialReportGenerator(data, self.mock_file)
        generator.generate_report()

        mock_doc_instance.build.assert_called()

if __name__ == '__main__':
    unittest.main()
