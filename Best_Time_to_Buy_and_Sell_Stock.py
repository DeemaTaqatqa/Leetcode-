def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    i=1
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit