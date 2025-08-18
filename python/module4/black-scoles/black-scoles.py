import math
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    try:
        if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
            raise ValueError("All inputs must be positive.")

        d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)

        call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        return round(call_price, 4)
    except Exception as e:
        print(f"Error calculating Black-Scholes price: {e}")
        return None