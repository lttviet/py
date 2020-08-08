from typing import List

def max_profit_buy_sell_once(prices: List[int]) -> int:
    """Given a list of stock prices
    Returns the max profit from buying and selling once.
    """
    min_price_seen, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit = max(max_profit, price - min_price_seen)
        min_price_seen = min(min_price_seen, price)

    return max_profit

if __name__ == '__main__':
    for lst in ([10,9,8,20], [20,9,8,6], [10,20,10,30]):
        print(lst, max_profit_buy_sell_once(lst))