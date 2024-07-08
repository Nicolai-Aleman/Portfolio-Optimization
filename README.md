# Portfolio Optimization Script

## Overview

This repository contains a Python script designed to optimize a portfolio of Exchange-Traded Funds (ETFs) to achieve the maximum Sharpe ratio. By utilizing historical data, it determines the optimal asset allocation to maximize returns relative to risk. The script makes use of the `yfinance` library to fetch financial data and the `scipy.optimize` module to perform the optimization.

## Features

- **Historical Data Fetching**: Retrieves historical adjusted closing prices for a specified list of ETFs.
- **Risk-Free Rate Calculation**: Fetches the yield of US Treasury bonds (e.g., the 10-Year Treasury Note) to use as the risk-free rate.
- **Return and Volatility Calculation**: Computes annualized returns and volatility for each ETF.
- **Portfolio Optimization**: Uses the Sharpe ratio as the optimization criterion to find the best combination of ETF weights.
- **Performance Metrics**: Outputs the optimized weights, expected return, volatility, and Sharpe ratio of the portfolio.

## Requirements

- Python 3.7+
- `yfinance` library
- `pandas` library
- `numpy` library
- `matplotlib` library
- `scipy` library

You can install the required libraries using pip:

```bash
pip install yfinance pandas numpy matplotlib scipy
