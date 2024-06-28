# Date & time imports
import time
import datetime as dt
import json

import os

cwd = os.getcwd()
# Webscraping
import requests

# Yahoo Finance imports
import yfinance as yf

import pandas as pd

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StockPriceYearRange:
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker.upper()

    """-------------------------------"""
    """-----------------------------------"""

    def _get_data_export_path(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return data["data_export_path"]

    """-----------------------------------"""

    def _get_chrome_driver_path(self):
        with open("config.json", "r") as file:
            data = json.load(file)
        return data["chrome_driver_path"]

    """-------------------------------"""

    def get_period_prices(self, period_start: str, period_end: str) -> dict:
        """
        :param period_start: A string that is the date of the quarter_start (Start of the quarter).
        :param period_end: A string that is the date of the quarter_end (End of the quarter).
        :return: Dictionary holding the high, low, average of the prices within the timeframe of the quarter.
        """

        quarter_data = {}

        # Split the dates into independent variables.
        start_year, start_month, start_day = period_start.split("-")
        end_year, end_month, end_day = period_end.split("-")

        # Turn all of the date elements into integers.
        start_year, start_month, start_day = (
            int(start_year),
            int(start_month),
            int(start_day),
        )
        end_year, end_month, end_day = int(end_year), int(end_month), int(end_day)

        # Create start and end dates for the first quarter of the year
        start_date = dt.datetime(start_year, start_month, start_day)
        end_date = dt.datetime(end_year, end_month, end_day)

        # Fetch the stock data for the specified ticker symbol and date range
        stock_data = yf.download(self.ticker, start=start_date, end=end_date)

        # Extract the 'High' and 'Low' columns from the stock data
        quarter_data["High"] = float(round(stock_data["High"].max(), 2))
        quarter_data["Low"] = float(round(stock_data["Low"].min(), 2))
        try:
            quarter_data["Average"] = float(round(stock_data["Adj Close"].mean(), 2))
        except ValueError:
            quarter_data["Average"] = "N\A"
        return quarter_data

    """-------------------------------"""

    def get_period_volume(self, period_start: str, period_end: str) -> dict:
        """
        :param period_start: A string that is the date of the quarter_start (Start of the quarter).
        :param period_end: A string that is the date of the quarter_end (End of the quarter).
        :return: Dictionary holding the high, low, average of the volume within the timeframe of the quarter.
        """
        quarter_data = {}

        # Split the dates into independent variables.
        start_year, start_month, start_day = period_start.split("-")
        end_year, end_month, end_day = period_end.split("-")

        # Turn all of the date elements into integers.
        start_year, start_month, start_day = (
            int(start_year),
            int(start_month),
            int(start_day),
        )
        end_year, end_month, end_day = int(end_year), int(end_month), int(end_day)

        # Create start and end dates for the first quarter of the year
        start_date = dt.datetime(start_year, start_month, start_day)
        end_date = dt.datetime(end_year, end_month, end_day)

        # Fetch the stock data for the specified ticker symbol and date range
        stock_data = yf.download(self.ticker, start=start_date, end=end_date)

        # Extract the 'High' and 'Low' columns from the stock data
        quarter_data["High"] = float(round(stock_data["Volume"].max(), 2))
        quarter_data["Low"] = float(round(stock_data["Volume"].min(), 2))
        try:
            quarter_data["Average"] = float(round(stock_data["Volume"].mean(), 2))
        except ValueError:
            quarter_data["Average"] = "N\A"
        return quarter_data


if __name__ == "__main__":

    sp = StockPriceYearRange("AMZN")

    prices = sp.get_period_prices("2024-01-01", "2024-03-31")
    volume = sp.get_period_volume("2024-01-01", "2024-03-31")
    print(f"Prices: {prices}")
    print(f"Volume: {volume}")
