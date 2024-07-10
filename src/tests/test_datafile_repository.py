import unittest
from unittest.mock import patch, mock_open
from repository.datafile_repository import FinancialDataFileRepository
from models.financial_entities import FinancialText

class FinancialDataFileRepositoryTestCase(unittest.TestCase):
    #create test data
    mock_text_content = 'Sample Text'
    mock_file = 'test.txt'
    @staticmethod
    def get_mock_financial_text():
        return FinancialText(content=FinancialDataFileRepositoryTestCase.mock_text_content)

    #test case
    @patch('builtins.open', new_callable=mock_open, read_data=mock_text_content)
    def test_get_all_data(self, mock_file):
        #Mock the file read part
        repo = FinancialDataFileRepository(self.mock_file)

        #get the mocked data
        data = repo.get_all_data()

        #assertions
        self.assertIsInstance(data, FinancialText)
        self.assertEqual(data.content, self.get_mock_financial_text().content)
        mock_file.assert_called_once_with(self.mock_file, 'r')


if __name__ == '__main__':
    unittest.main()
