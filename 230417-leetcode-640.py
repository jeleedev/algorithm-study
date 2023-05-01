'''
https://leetcode.com/problems/lfu-cache/

문제풀이 참고
https://yuminlee2.medium.com/leetcode-460-lfu-cache-a974db16f24a
https://memorylimitexceeded.gitlab.io/leetcode/problems/0460-lfu-cache.html
'''


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.frequencyMap = dict()
        self.minFreq = 0

    def get(self, key: int) -> int:
        # 1. cache list에 key가 없으면 -1, 있으면 값 리턴
        if key not in cache:
            return -1
        return cache[key]

        # 2. frequency 계산
        self.frequencyMap[tempNode.freq].removeNode(tempNode)
        if self.frequencyMap[tempNode.freq].head is None:
            del self.frequencyMap[tempNode.freq]
            if self.minFreq == tempNode.freq:
                self.minFreq += 1

        self.cache[key].freq += 1
        self.frequencyMap[self.cache[key].freq].insertAtTail(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        # 예외처리
        if self.capacity == 0:
            return

        # 1. cache list에 key가 있으면 get(key)
        if key in cache:
            self.get(key)
            # self.cache[key].value = value ????
            return

        # size가 capacity에 도달하면 가장 적게 사용된 키 제거
        if self.size == self.capacity:
            # del self.cache[self.frequencyMap[self.minFreq].head.key]
            # self.frequencyMap[self.minFreq].removeHead()
            # if self.frequencyMap[self.minFreq].head is None:
            #     del self.frequencyMap[self.minFreq]
            self.size -= 1

        self.minFreq = 1
        self.cache[key] = LinkedListNode(key, value, self.minFreq)
        self.frequencyMap[self.cache[key].freq].insertAtTail(self.cache[key])
        self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
