#Старая задача перед собеседованием в Facebook
#Выведите таблицу размером n*n, заполненную числами
#от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по
#часовой стрелке:

#РЕШЕНИЕ 1
n=int(input('введи '))
q=n**2
k=1
g=0
h=-1
m=0
a=[[0 for j in range(n)] for i in range(n)]
while True:
    for i in range(g,n,1):
        a[m][i]=k
        k+=1
    g+=1
    for i in range(g,n,1):
        a[i][n-1]=k
        k+=1
    for i in range(n-2,h,-1):
        a[n-1][i]=k
        k+=1
    h+=1
    for i in range(n-2,h,-1):
        a[i][m]=k
        k+=1
    n-=1
    m+=1
    if k>q:
        break
for i in range(len(a)):
    print(a[i])

#Более оптимальное решение
n=int(input())
t=[[0]*n for i in range (n)]
i,j=0,0
for k in range(1, n*n+1):
  t[i][j]=k
  if k==n*n: break
  if i<=j+1 and i+j<n-1: j+=1
  elif i<j and i+j>=n-1: i+=1
  elif i>=j and i+j>n-1: j-=1
  elif i>j+1 and i+j<=n-1: i-=1
for i in range(n):
  print(*t[i])
