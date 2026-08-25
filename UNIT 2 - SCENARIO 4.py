# House Robber Problem using Dynamic Programming

# Accept amount in each house
houses = list(map(int, input("Enter amounts in houses: ").split()))

n = len(houses)

# Handle empty input
if n == 0:
    print("Maximum amount = 0")

elif n == 1:
    print("Maximum amount =", houses[0])

else:
    # dp[i] = maximum amount that can be collected
    # from first i houses
    dp = [0] * n

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        # Either skip current house or rob current house
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    print("Maximum possible amount =", dp[n - 1])
