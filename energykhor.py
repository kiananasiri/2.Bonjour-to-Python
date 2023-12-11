"""lambda"""
n , k = map(int , input().split())
a = [[0]*2 for j in range(n)]
for i in range(n):
    a[i][0] , a[i][1] = map(int , input().split())
a = sorted(a , key = lambda x : x[0])
#print(sort_array)
for i in range(n):
    if a[i][1] >= a[i][0] and k >= a[i][0]:
        k += a[i][1] - a[i][0]
print(k)
