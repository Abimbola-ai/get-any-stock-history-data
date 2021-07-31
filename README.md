# Get any stock price history from yahoo finance


This is a tool that can be used to get the historical price of any ticker for yahoo finance website. The following data will be returned:

* `timestamp`: Datetime stamp
* `adjclose`: adjusted closing price of the stock on any given day
* `high`: highest price of the stock daily
* `volume`: volume of the stock daily
* `open`: opening price of the stock on any given day
* `low`: lowest price of the stock daily
* `close`: price at which the stock stopped trading during normal trading hours

## Installation

Use a python interface
to run `pip install git+https://github.com/Abimbola-ai/get-any-stock-history-data` to install the package.

## Usage

### How to use the package?

To use the package, call the `get_data` function to get daily data for the `ticker` and `year` specified into the function. This will return a dataframe that can be saved into `.csv` file.

```
get_data(ticker,years)
```

For example:

```
get_data(AAPL, 5)
```

Returns a `AAPL.csv` file Apple stocks for 5 years.

Other methods are `.subtract, .multipy(), .divide(), .nroot().`

What is what:

- [ScraperModule](/stocks/scaper.py) contains the scraping function and its dependencies;


