import time



# Max profit

class Solution:
    def maxProfit(self, prices) -> int:

        max_profit = 0  # Initialize profit

        # Iterate through the prices array
        for i in range(1, len(prices)):
            # If the price difference is positive, add it to the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit


# Measure runtime
start_time = time.time()  # Record start time
print(Solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]))  # Call the function
end_time = time.time()  # Record end time

print(f"Runtime: {end_time - start_time:.6f} seconds")


# or this
def max_profit():
    prices = [7, 1, 5, 3, 6, 4]
    index_of_min = prices.index(min(prices))
    len_prices = len(prices)

    if index_of_min == len_prices:
        print(0)
    profits = []
    for i in range(index_of_min, len_prices):
        if prices[i] > prices[i - 1]:
            profits.append(prices[i] - prices[i - 1])
    return sum(profits)


# Measure runtime
start_time = time.time()  # Record start time
max_profit()  # Call the function
end_time = time.time()  # Record end time

print(f"Runtime: {end_time - start_time:.6f} seconds")

