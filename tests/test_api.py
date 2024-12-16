import unittest
from unittest.mock import patch, MagicMock

import requests

from src.api import get_crypto_price, get_historical_price


class TestApi(unittest.TestCase):

    @patch('src.api.requests.get')
    def test_get_crypto_price_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'bitcoin': {'usd': 29000}}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        price = get_crypto_price('bitcoin')
        self.assertEqual(price, 29000)

    @patch('src.api.requests.get')
    def test_get_crypto_price_coin_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {}  # Response with no coin data
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        price = get_crypto_price('nonexistentcoin')
        self.assertEqual(price, "Coin not found")

    @patch('src.api.requests.get')
    def test_get_crypto_price_request_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network Error")
        price = get_crypto_price('bitcoin')
        self.assertEqual(price, "Error fetching data: Network Error")

    @patch('src.api.requests.get')
    def test_get_historical_price_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'prices': [[1678886400000, 29000], [1678972800000, 30000]]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        historical_data = get_historical_price('bitcoin')
        self.assertEqual(len(historical_data), 2)

    @patch('src.api.requests.get')
    def test_get_historical_price_request_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network Error")
        historical_data = get_historical_price('bitcoin')
        self.assertIsNone(historical_data)

    @patch('src.api.requests.get')
    def test_get_historical_price_key_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        historical_data = get_historical_price('bitcoin')
        self.assertIsNone(historical_data)


if __name__ == '__main__':
    unittest.main()