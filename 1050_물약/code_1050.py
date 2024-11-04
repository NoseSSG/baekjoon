# https://www.acmicpc.net/problem/1050
import sys

# sys.stdin = open('input_1050.txt','r')
N,M = map(int,input().split())

def find_cost(menu):
    if isinstance(menu,int):
        return menu
    cnt = int(menu[0])
    need = menu[1:]
    if need in ingredients:
        return cnt * ingredients[need]
    tt = float('inf')
    for n in potions[need]:
        temp = 0
        for m in n:
            temp += find_cost(m)
        tt = min(temp,tt)
    ingredients[need] = tt
    return cnt*ingredients[need]


love_ans = float('inf')
ingredients = {}
for _ in range(N):
    ingredient,cost = map(str,input().split())
    ingredients[ingredient] = int(cost)
    if ingredient == 'LOVE':
        love_ans = int(cost)

potions = {}
for _ in range(M):
    potion,recipe = map(str,input().split('='))
    if potion not in potions:
        potions[potion] = []
    potions[potion].append(list(map(str,recipe.split('+'))))


if "LOVE" not in ingredients and "LOVE" not in potions:
    love_ans = -1
elif "LOVE" not in potions:
    love_ans = ingredients["LOVE"]
else:
    for needs in potions["LOVE"]:
        temp = 0
        for n in needs:
            temp += find_cost(n)
        love_ans = min(love_ans,temp)
print(love_ans)