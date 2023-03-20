'''
https://leetcode.com/problems/minimum-cost-for-tickets/

문제풀이 참고. https://mia-dahae.tistory.com/158
'''
def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    lastDay = days[len(days)-1]
    isIncluded = [0 for i in range(lastDay+1)]
    minCosts = [0 for i in range(lastDay+1)]

    for day in days:
        isIncluded[day] = True

    for i in range(len(minCosts)):
        if isIncluded[i] == False:
            minCosts[i] = minCosts[i-1]
            continue
        
        # day 1
        one = minCosts[i-1]+costs[0]
        # day 7
        seven = minCosts[max(0, i-7)]+costs[1]
        # day 30
        thirty = minCosts[max(0, i-30)]+costs[2]

        minCosts[i] = min(one, min(seven, thirty))
    
    return minCosts[lastDay]