def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


prices = [1,2,3,4,5,6,7]

print(max_profit(prices))