# StockPriceRange Scraper

- Get the high, low, and average of a stock price during a period.

---

### Setup

1. Clone git repository: `https://github.com/PrimalFinance/StockPriceRangeScraper.git`
2. Install the projects requirements with `pip install -r requirements.txt`

---

### Instructions

- Create a class instance.

```
    sp = StockPriceRange("AMZN")
```

###### get_period_prices(str, str)

- Get the high, low, and average price during Q124 for Amazon.

```
    prices = sp.get_period_prices("2024-01-01", "2024-03-31")

    # Output
     {'High': 181.7, 'Low': 144.05, 'Average': 166.93}
```

###### get_period_volume(str, str)

- Get the high, low, and average volume during Q124 for Amazon.

```
    volume = sp.get_period_volume("2024-01-01", "2024-03-31")

    # Output
    {'High': 117154900.0, 'Low': 26880900.0, 'Average': 44267786.89}
```
