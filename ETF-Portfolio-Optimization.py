import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the list of ETFs
etfs = ['SPY', 'VOO', 'VTI', 'DIA']

# Fetch historical data for ETFs
data = yf.download(etfs, start="2020-01-01", end="2024-01-01")['Adj Close']

# Calculate daily returns
returns = data.pct_change().dropna()

# Fetch the yield of US Treasury bonds (e.g., 10-year)
treasury_yield = yf.Ticker("^TNX")
treasury_data = treasury_yield.history(start="2020-01-01", end="2024-01-01")
risk_free_rate = treasury_data['Close'].iloc[-1] / 100

# Calculate annualized return and volatility
annual_returns = returns.mean() * 252
annual_volatility = returns.std() * np.sqrt(252)

# Portfolio performance
def portfolio_performance(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    return portfolio_return, portfolio_volatility

# Objective function to minimize (negative Sharpe ratio)
def negative_sharpe_ratio(weights, returns, risk_free_rate):
    portfolio_return, portfolio_volatility = portfolio_performance(weights, returns)
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    return -sharpe_ratio

# Number of assets
num_assets = len(etfs)

# Randomly initialize portfolio weights
weights = np.random.random(num_assets)
weights /= np.sum(weights)

# Constraints and bounds
constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
bounds = tuple((0, 1) for _ in range(num_assets))

# Optimize portfolio
result = minimize(negative_sharpe_ratio, weights, args=(returns, risk_free_rate), method='SLSQP', bounds=bounds, constraints=constraints)

# Optimized weights
optimized_weights = result.x

# Optimized portfolio performance
optimized_return, optimized_volatility = portfolio_performance(optimized_weights, returns)
optimized_sharpe_ratio = (optimized_return - risk_free_rate) / optimized_volatility

# Display the optimized portfolio
optimized_weights_percent = optimized_weights * 100

print("Optimized Weights (in %):")
for i, weight in enumerate(optimized_weights_percent):
    print(f"{etfs[i]}: {weight:.2f}%")

print("Optimized Return:", optimized_return)
print("Optimized Volatility:", optimized_volatility)
print("Optimized Sharpe Ratio:", optimized_sharpe_ratio)
