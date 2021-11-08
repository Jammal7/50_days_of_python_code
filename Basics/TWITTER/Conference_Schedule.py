def maxPresentations(scheduleStart, scheduleEnd):
    # Write your code here
    sch = []
    N = len(scheduleEnd)
    for i in range(N):
        sch.append([scheduleStart[i], scheduleEnd[i]])
    
    sch.sort(key = lambda x: x[1])
    me = float('-inf')
    cnt = 0
    
    for i, curr in enumerate(sch):
        s,e = curr
        if s >= me:
            cnt += 1
            me = e
    return cnt