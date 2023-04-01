def start():
    A = [
        [1,2,0],
        [4,5,6],
        [7,8,9]
    ]
    suma = 0
    blackList = []
    for i in range(0, len(A[1])):
        for j in range(0, len(A[1])):
            if j not in blackList:
                suma += A[i][j]
            else:
                print("no sumamos este numero", A[i][j])
            if (A[i][j]) == 0:
                blackList.append(j)
                print(j)

    print(blackList)
    print(suma)
if __name__ == '__main__':
    start()