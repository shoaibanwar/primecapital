import unittest
from unittest.mock import patch, MagicMock
from models.report_request import FinancialReportRequest
from models.report_response import FinancialReportResponse

class FinancialReportRequestTestCase(unittest.TestCase):
    @patch('models.report_request.FinancialDataGateway')
    def test_manage(self, MockGateway):
        mock_gateway_instance = MockGateway.return_value
        mock_gateway_instance.fetch_data.return_value = MagicMock()

        request = FinancialReportRequest(('TABLE', 'TEXT'))
        response = request.manage()

        self.assertIsInstance(response, FinancialReportResponse)
        MockGateway.assert_called()

if __name__ == '__main__':
    unittest.main()