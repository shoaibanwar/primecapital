import unittest
from unittest.mock import patch
from repository.database_repository import FinancialDataBaseRepository
from models.financial_entities import FinancialTable

class FinancialDataBaseRepositoryTestCase(unittest.TestCase):
    mock_test_data = [[1, 'Test Report', 100.0]]
    mock_file = 'test.db'
    #create test data
    @staticmethod
    def get_mock_financial_table():
        return FinancialTable(data=FinancialDataBaseRepositoryTestCase.mock_test_data)
    

    @patch('repository.database_repository.FinancialDatabase')
    def test_get_all_data(self, MockDatabase):
        #Mock the database read part
        mock_financial_table = self.get_mock_financial_table()
        mock_database_instance = MockDatabase.return_value
        mock_database_instance.get_all_data.return_value = mock_financial_table

        #get the mocked from repository
        repo = FinancialDataBaseRepository(self.mock_file)
        data = repo.get_all_data()

        #assertions
        self.assertIsInstance(data, FinancialTable)
        self.assertEqual(data, mock_financial_table)
        MockDatabase.assert_called_once_with(self.mock_file)

if __name__ == '__main__':
    unittest.main()
