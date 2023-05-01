'''
슬라이딩 윈도우 문제
https://leetcode.com/problems/fruit-into-baskets
'''


def totalFruit(fruits):
    baskets = dict()
    prev = result = 0

    for fruit in fruits:
        if fruit in baskets:
            baskets[fruit] += 1
        else:
            baskets[fruit] = 1

        if len(baskets) > 2:
            baskets[fruits[prev]] -= 1
            if baskets[fruits[prev]] == 0:
                del baskets[fruits[prev]]
            prev += 1
        else:
            result = max(result, sum(baskets.values()))

    return result


fruits = [0, 1, 2, 2]
totalFruit(fruits)

'''
fruites = [0,1,2,2]

-----------------------------
{0: 1}
maximum number of fruits 1
-----------------------------
{0: 1, 1: 1}
maximum number of fruits 2
-----------------------------
{0: 1, 1: 1, 2: 1}
maximum number of fruits 2
-----------------------------
{1: 1, 2: 2}
maximum number of fruits 3
'''
