def hackerCards(collection, d):
    # Write your code here
    cs = set(collection)
    N = len(collection)
    possible = {i for i in range(1, N+1)}
    available = sorted(possible - cs)
    cnt = []
    
    for i, num in enumerate(available):
        if d - num >= 0:
            d -= num
            cnt.append(num)
        else:
            return cnt
    if available:
        num = available[-1] + 1
    else:
        num = max(collection) + 1
    
    while d >= 0:
        if num in cs:
            num += 1
            continue
        if d-num >= 0:
            d -= num
            cnt.append(num)
        else:
            return cnt
        num += 1
    return cnt