'''
https://school.programmers.co.kr/learn/courses/30/lessons/42587
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(value, index) for index, value in enumerate(priorities)])

    while queue:
      cur = queue.popleft()
      # 우선순위가 더 높은 게 있으면 대기목록 맨 마지막으로 보낸다
      # if queue 조건을 빼면 런타임 에러 🤔
      if queue and max(queue)[0] > cur[0]:
        queue.append(cur)
      # 인쇄된 카운트 넘버링
      else:
        answer += 1
        if cur[1] == location: break
    return answer
  
  
'''
  note.
  - 튜플 자료형을 사용해서 (index, value)를 묶어서 처리
    - 튜플: 여러 타입의 값을 넣을 수 있음. 읽기만 가능. 수정불가
  - deque 사용
    - list보다 속도가 훨씬 빠르다 > list O(n), deque는 O(1) 
    - 양방향으로 요소를 추가/제거 가능
    - 참고 (https://codingpractices.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%99%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%8C%80%EC%8B%A0-%ED%81%90-%EB%8D%B0%ED%81%AC-deque-%EB%A5%BC-%EC%93%B8%EA%B9%8C)
'''