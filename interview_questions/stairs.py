# Dynamic Programming (Top Down)
def climb_memoization(n, memo={}):
    if n <= 1:
        return 1
    if n not in memo:
        memo[n] = climb_memoization(n-1, memo) + climb_memoization(n-2, memo)
    return memo[n]

# Dynamic Programming (Bottom-Up)
def climb_tabulation(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    print(dp)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climb_tabulation(5))


# Recursive Tree
def climb_tree(n):
    if n <= 1:
        return 1
    return climb_tree(n-1) + climb_tree(n-2)



