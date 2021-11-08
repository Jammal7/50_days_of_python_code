from collections import Counter
def stockPairs(stocksProfit, target):
    # Write your code here
    sp = list(set(stocksProfit))
    seen = set()
    cnt = 0
    cp = Counter(stocksProfit)
    
    for k,v in cp.items():
        if k * 2 == target and v > 1:
            cnt += 1
    for i, num in enumerate(sp):
        if target - num in seen:
            cnt += 1
        seen.add(num)
    return cnt