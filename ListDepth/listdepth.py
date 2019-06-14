def depth(L):
    if not isinstance(L, list):
        return 0
    ans = 0
    for value in L:
        ans = max(ans, depth(value) + 1)
    return ans
 
def depthstr(L):
    L = str(L)
    record = 0
    count =0
    for i in range(0,len(L)):
        count += (L[i] == '[')
        count -= (L[i] == ']')
        record = max(record, count)
    return record

L=[1,2,3,[4,[5,6]]]
print (depth(L))
print (depthstr(L))
