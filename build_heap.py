import os


def change(data,size,i,swaps):
    kp,lp = 2*i+1,2*i+2
    maxed = i
    if kp < size and data[kp] < data[maxed]:
        maxed = kp
    if lp < size and data[lp] < data[maxed]:
        maxed = lp
    if i != maxed:
        data[i], data[maxed] = data[maxed], data[i]
        swaps.append((i, maxed))
        change(data,size,maxed,swaps)


def sorter(data,size):
    swaps = []
    for i in range(size//2,-1,-1):
        change(data,size,i,swaps)
    return swaps


def main():
    first_input = input()
    if first_input.__contains__('I'):
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = sorter(data,n)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    elif first_input.__contains__('F'):
        file_name = input()
        if file_name.__contains__('a'):
            print("INPUT-OUTPUT ERROR")
            return
        with open("./tests/" + file_name) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
            swaps = sorter(data,n)
            print(len(swaps))
            for i, j in swaps:
                print(i, j)
    else:
        print("INPUT-OUTPUT ERROR")
        return
main()
