# A classic example of an optimization problem involves making change using the fewest coins. Suppose you are a programmer
# for a vending machine manufacturer. Your company wants to streamline effort by giving out the fewest possible coins in
# change for each transaction. Suppose a customer puts in a dollar bill and purchases an item for 37 cents. What is the
# smallest number of coins you can use to make change? The answer is six coins: two quarters, one dime, and three
# pennies. How did we arrive at the answer of six coins? We start with the largest coin in our arsenal (a quarter) and
# use as many of those as possible, then we go to the next lowest coin value and use as many of those as possible.
# This first approach is called a greedy method because we try to solve as big a piece of the problem
# as possible right away.


#GREEDY METHOD

def greedy_machine(change, coin_list):
    coin_list.sort(reverse=True)
    current = 0
    change_coin_list = []
    i = -1
    while current < change:
        i += 1
        while coin_list[i] + current <= change:
            current = coin_list[i] + current
            change_coin_list.append(coin_list[i])

    return change_coin_list

print(greedy_machine(63, [1, 5, 10, 21, 25]))


#FIRST RECURSIVE METHOD
# Massively inneficient. Test case below makes 67,716,925 recursive calls

def rec_mc(coin_value_list, change):
    min_coins = change

    if change in coin_value_list:
        return 1

    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_mc(coin_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
            return min_coins

# print(rec_mc([1,5,10,25], 63))

# A BETTER APPROACH (BUT NOT QUITE DYNAMIC PROGRAMMING)
# Remembering the results in a table (MEMOIZATION, OR CACHING)

def recDC(coinValueList, change, knownResults):
    print(knownResults)
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i,
                                 knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


# print(recDC([1, 5, 10, 25], 63, [0] * 64))

#A DYNAMIC FUNCTION (Most efficient)
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()

