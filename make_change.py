def make_change(coins, total):
    
    """Computes the minimum number of coins (of given denominations) required to make a given total.
    It is assumed that a 1 pence coin is available, otherwise the problem may have no solution.
    
    coins = a list of coin denominations in any order (1 pence can be included but it is assumed anyway)
    total = the total to be made    """
    
    m = [[0 for t in range(total)] for c in range(len(coins)+1)]  #initialise with zeros
    
    #m[i][j] = minimum number of coins required to make j pence by using coins attributed to rows <= row i
    #first row is attributed to 1p coin by default. Rows thereafter are attributed to coins in the order in which
    #they are listed in 'coins'
    
    for t in range(1, total+1):    #attribute first row to 1p coin. Min no. of 1p coins needed to make x pence is x
        m[0][t-1] = t
    
    for c in range(len(coins)):     #for each coin
            
        for t in range(1, total+1):    #for each positive integer less than or equal to the total
                        
            if coins[c] == t:    #if current coin is equal to current total, then current total can be made with one coin
                m[c+1][t-1] = 1
        
            elif coins[c] > t:    #if current coin is larger than current total, use solution using previous coins
                m[c+1][t-1] = m[c][t-1]
        
            else:
                #if we can use current coin, then optimal solution is the minimum of:
        
                m[c+1][t-1] = min(m[c][t-1],      #solution using previous coins
                          1 + m[c+1][t-1 - coins[c]])   #1 coin + no. of coins needed to make up (current total - current coin)

    return(m[-1][-1])    
