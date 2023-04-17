### dict 와 defaultdict 차이

    - defaultdict는 dict 클래스의 서브 클래스
    - dict으로 사용하면 key의 값이 없거나 없는 key를 조작할려할 때 keyError가 발생하는데 이를 보완한 것이 defaultdict
    - defaultdict에서는 사용자가 없는 key를 접근 or 조작할 때 key 값이 없다면 defaultdict 쪽에서 key를 만들고 defualt 값을 자체적으로 생성해줌. 이 기능이 dictionaries에서 missing key 문제를 해결해준다.

dict으로 풀 때 keyError가 안나게 하려면 (if n in dic) 이렇게 해야하기 때문에 오히려 효율이 떨어짐
