import unittest
from unittest import mock
from requests.models import Response
from calculate_volatility import VolatilityScript
import datetime


class TestVolatilityScript(unittest.TestCase):
    def setUp(self) -> None:
        self.start_date = datetime.date(2023, 7, 6)
        self.end_date = datetime.date(2023, 7, 7)
        self.vs = VolatilityScript("EURUSD", self.start_date, self.end_date)

    def tearDown(self) -> None:
        self.vs = None

    def test_latest_ohlc_data(self):
        with mock.patch("requests.get") as mk_get:
            data = [
                {'close': 1.08895, 'date': '2023-07-06', 'high': 1.09008, 'low': 1.08339, 'open': 1.08569},
                {'close': 1.09661, 'date': '2023-07-07', 'high': 1.09734, 'low': 1.08672, 'open': 1.08896},
            ]

            mk_response = Response()
            mk_response.json = mock.MagicMock(return_value={"quotes": data})
            mk_get.return_value = mk_response

            ohlc_data, prices = self.vs.latest_ohlc_data()
            self.assertEqual(ohlc_data, data)
            self.assertEqual(prices, [d["close"] for d in data])

            url = "https://marketdata.tradermade.com/api/v1/timeseries"
            querystr = {
                "currency": "EURUSD",
                "start_date": self.start_date,
                "end_date": self.end_date,
                "api_key": "i8dTtXjDgQILmcQVzN1I"
            }
            mk_get.assert_called_once_with(url, params=querystr)

    def test_calc_historical_volatility_raises(self):
        prices = [100]

        with self.assertRaises(Exception):
            self.vs.calc_historical_volatility(prices)


if __name__ == "__main__":
    unittest.main()
