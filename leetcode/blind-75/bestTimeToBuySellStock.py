from typing import List

def maxProfit(prices: List[int])->int:
    profit=0
    buy=prices[0]
    for stockPrice in prices[1:]:
        if stockPrice>buy:
            profit = max(profit, stockPrice-buy)
        else:
            buy = stockPrice
    return profit


print("Input stock prices",end=": ")
prices = [int(ele) for ele in input().split()]
max_profit = maxProfit(prices)
print(max_profit)