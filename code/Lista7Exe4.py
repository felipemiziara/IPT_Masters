import math

def verificaHeap(v, n):
    max = -1
    isHeap = False
    for i in range(0,  math.floor(n/2)):
        left = 2*i + 1
        right = 2*1 + 2
        if(v[i] >= v[left] and v[i] >= v[right]):
            print(i)
            isHeap = True
        else:
            isHeap = False
        if(v[i] > max):
            max = v[i]
    return isHeap

vector = [16,14,10,8,7,9,3,2,4,1]

print(verificaHeap(vector, len(vector)))