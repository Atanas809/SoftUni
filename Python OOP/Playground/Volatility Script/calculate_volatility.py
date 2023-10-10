import datetime

import requests
import numpy as np


class VolatilityScript:
    _prev_date = datetime.date.today() - datetime.timedelta(days=1)

    def __init__(self, currency, start_date, end_date=_prev_date, weighting=1.6):
        self.currency = currency
        self.start_date = start_date
        self.end_date = end_date
        self.weighting = weighting

    def latest_ohlc_data(self):
        url = "https://marketdata.tradermade.com/api/v1/timeseries"
        querystr = {
            "currency": self.currency,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "api_key": "i8dTtXjDgQILmcQVzN1I"
        }
        response = requests.get(url, params=querystr)
        data = response.json()

        if "quotes" in data:
            ohlc_data = response.json()["quotes"]
            prices = [d["close"] for d in ohlc_data]
            return ohlc_data, prices
        raise Exception(f"No OHLC data found for {self.currency}")

    def calc_historical_volatility(self, prices: list):
        if len(prices) == 1:
            raise Exception("Can't calculate historical volatility because price observation must be more than one!")

        log_returns = [np.log(prices[i]) / np.log(prices[i - 1]) for i in range(1, len(prices))]
        squared = [l ** 2 for l in log_returns]
        avg = sum(squared) / len(squared)
        hv = np.sqrt(avg) * np.sqrt(252)
        return hv

    def calc_volatility(self, ohlc_data):
        closes = [float(bar["close"]) for bar in ohlc_data]
        vol = np.std(closes) * np.sqrt(252)
        return vol

    def multiplier(self):
        return self.weighting

    def calc_optionblitz_volatility(self):
        ohlc_data, prices = vs.latest_ohlc_data()
        hv = self.calc_historical_volatility(prices)
        vol = self.calc_volatility(ohlc_data)
        optionblitz_vol = max(hv, vol) * self.multiplier()
        return f"{optionblitz_vol:.5f}"


start_date = datetime.date(2023, 7, 1)
end_date = datetime.date(2023, 7, 10)
vs = VolatilityScript("EURUSD", start_date)
print(vs.calc_optionblitz_volatility())
