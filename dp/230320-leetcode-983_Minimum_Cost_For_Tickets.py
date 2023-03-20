'''
https://leetcode.com/problems/minimum-cost-for-tickets/
'''

# 풀이 1: 일반적인 재귀호출
def fib(self, n: int) -> int:
    if n < 2 : 
        return n
    return self.fib(n-1) + self.fib(n-2)

# 풀이 2: dict 사용
def fib(self, n: int) -> int:
    dic = dict()

    if n < 2:
        return n

    if n in dic:
        return dic[n]

    dic[n] = self.fib(n - 2) + self.fib(n - 1)

    return dic[n]
  
# 풀이 3: defaultdict 사용
dp = collections.defaultdict(int)

def fib(self, n: int) -> int:
    if n < 2:
        return n
    
    if self.dp[n]:
        return self.dp[n]

    self.dp[n] = self.fib(n-2) + self.fib(n-1)
    
    return self.dp[n]