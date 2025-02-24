# https://www.acmicpc.net/problem/14725
import sys
sys.stdin = open('input_14725.txt')

def add_tree(tree,small_route):
    if len(small_route) == 0:
        return
    if small_route[0] not in tree:
        tree[small_route[0]] = {}
    add_tree(tree[small_route[0]],small_route[1:])
    
def print_Tree(tree,length):
    for i in sorted(tree.keys()):
        print('--'*length,end='')
        print(i)
        print_Tree(tree[i],length + 1)


n = int(input())
routes = [list(map(str,input().split())) for _ in range(n)]
trees = {}


for route in routes:
    r = route[1:]
    add_tree(trees,r)

print_Tree(trees,0)