import sys

n = sys.argv[1]
m = sys.argv[2]

def seq(n,m):
    path = '1'

    for idx in range(m-1, n*m, m-1):
        pathItem = idx % n + 1
        if pathItem == 1:
            return path
        path = path + str(pathItem)

print(seq(int(n),int(m)))
