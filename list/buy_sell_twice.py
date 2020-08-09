from typing import List

def max_profit_buy_sell_twice(prices: List[int]) -> int:
    """Given a list of stock prices
    Returns the max profit from buying and selling twice.
    You must sell the 1st stock before buying the second stock.
    """
    # https://cs.stackexchange.com/questions/60668/
    # max(s1 - b1 + s2 - b2)
    # max(s1 - b1 - b2)
    # max(s1 - b1)
    min_price, max_profit_first_sell = float('inf'), 0.0
    max_profit_second_buy, max_profit_second_sell = float('-inf'), 0.0

    for price in prices:
        max_profit_first_sell = max(max_profit_first_sell, price - min_price)
        min_price = min(min_price, price)
        max_profit_second_buy = max(max_profit_second_buy, max_profit_first_sell - price)
        max_profit_second_sell = max(max_profit_second_sell, max_profit_second_buy + price)

    return max_profit_second_sell

def max_profit_buy_sell_twice_2(prices: List[int]) -> int:
    # max profit 1st sell at <= time i
    # max profit 2nd sell at >= time i
    min_price, max_profit = float('inf'), 0.0

    max_profit_first_sell = [0] * len(prices)
    # forward, max profit by selling 1st stock at time i
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
        max_profit_first_sell[i] = max_profit

    # backward, max profit by selling 2nd stock at time i
    max_price = float('-inf')
    for i in reversed(range(1, len(prices))):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, max_price - prices[i] + max_profit_first_sell[i-1])

    return max_profit

if __name__ == '__main__':
    for lst in ([10,11,9,20], [20,9,8,6], [10,20,10,30], [1,10]):
        print(lst, max_profit_buy_sell_twice(lst))
        print(lst, max_profit_buy_sell_twice_2(lst))