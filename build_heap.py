import os

def bh(data,i,x,swaps):
    while(True):
        kp, lp = i*2+1, i*2+2
        if max(kp,lp) < x:
            if data[i] >= max(data[kp], data[lp]):
                break
            elif data[kp] > data[lp]:
                swaps = change(data,i,kp,swaps)
                i = kp
            else:
                swaps = change(data, i, lp,swaps)
                i = lp
        else:
            break
    return swaps
def change(data,i,j,swaps):
    data[i],data[j] = data[j],data[i]
    swaps.append(i), swaps.append(j)
    return swaps

def sorter(data,size):
    swaps = []
    for k in range(size-1,0,-1):
        swaps = change(data,0,k,swaps)
        swaps = bh(data,0,k,swaps)
    return swaps

def main():
    first_input = input()
    if first_input.__contains__('I'):
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        sorter(data,n)
        for a in data:
            print(a,end='')
    elif first_input.__contains__('F'):
        file_name = input()
        if file_name.__contains__('a'):
            print("INPUT-OUTPUT ERROR")
            return
        file = os.path.join(os.getcwd(), 'test', file_name)
        with open(file) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
            sorter(data,n)
            for a in data:
                print(a, end='')
    else:
        print("INPUT-OUTPUT ERROR")
        return
main()