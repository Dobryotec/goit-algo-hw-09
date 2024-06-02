coins=[50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum, coins):
    result = {}
    for coin in coins:
        if sum >= coin:
            num_coins = sum // coin
            sum -= num_coins * coin
            result[coin] = num_coins

        if sum == 0:
            break

    return result

print(find_coins_greedy(498, coins))

def find_min_coins(sum, coins):
    min_coins = [0] + [float('inf')] * sum
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while sum > 0:
        coin = coin_used[sum]
        result[coin] = result.get(coin, 0) + 1
        sum -= coin
    
    return dict(sorted(result.items()))    

print(find_min_coins(498, coins))