import numpy as np
import pandas as pd

def get_prices(tickers, start_date):
    """Download daily prices. Returns a table: one row per day, one column per ticker."""
    import yfinance as yf  # imported here so the tests do not need yfinance or internet

    data = yf.download(tickers, start=start_date, auto_adjust=True, progress=False)
    prices = data["Close"]
    if isinstance(prices, pd.Series):            # happens with a single ticker
        prices = prices.to_frame(tickers[0])

    bad = [t for t in tickers if t not in prices.columns or prices[t].isna().all()]
    if bad:
        raise ValueError(f"No data found for: {bad}. Check the symbols on finance.yahoo.com.")

    prices = prices[tickers]
    return prices.dropna() 

def get_returns(prices):
    """Daily percentage change of each asset (simple returns)."""
    return prices.pct_change().dropna()