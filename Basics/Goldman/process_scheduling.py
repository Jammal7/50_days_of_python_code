import heapq

def minimumTime(ability, processes):
    heap = list(map(lambda x: -x, ability))
    heapq.heapify(heap)
    ans = 0
    while processes > 0:
        curr = heapq.heappop(heap)
        processes += curr
        heapq.heappush(heap, -(-curr // 2))
        ans += 1
    return ans